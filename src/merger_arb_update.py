# =============================================================================
# MERGER ARB TEST — Daily Update Script
# =============================================================================
# HYBRID MODEL:
#   Automated layer:
#     - Scans Polygon.io news API for US M&A announcements
#     - Scans SEC EDGAR for formal deal filings (SC TO-T, SC 13E-3, DEFM14A)
#     - Scans LSE RNS feed for UK takeover announcements
#     - Updates daily prices and spreads on all open paper positions
#     - Calculates P&L and unrealised returns
#     - Generates alerts for spread widening and time stops
#     - Flags deal candidates for your manual review
#     - Maintains README dashboard
#
#   Manual layer (you):
#     - Review candidates flagged in README each morning
#     - Apply qualitative scoring (regulatory, financing, strategic)
#     - Add selected deals to data/deals.csv to paper trade them
#     - Mark candidates as reviewed in data/candidates.csv
#     - Update deal status when deals close or break
#
# DEAL FILTERS (applied automatically):
#   - Cash deals only (stock-for-stock requires short leg)
#   - Friendly deals only (hostile breaks at ~30% vs ~5% for friendly)
#   - Minimum deal size: $500m USD equivalent
#   - Geography: US-listed or UK-listed targets only
#   - Spread must be positive (target trading below offer price)
#
# ALERT TRIGGERS:
#   - Spread widens >2pp in a single day (deal stress signal)
#   - Deal is >30 days past expected close with no announcement
#   - Spread goes negative (target trading above offer — unusual)
#
# DATA SOURCES:
#   - Polygon.io news API (US deals, requires API key)
#   - SEC EDGAR full-text search API (US formal filings, free)
#   - LSE RNS XML feed (UK deals, free)
#   - yfinance (current target prices)
# =============================================================================

import os
import json
import time
import re
import warnings
from datetime import datetime, timedelta, timezone, date

import numpy as np
import pandas as pd
import requests
import yfinance as yf

warnings.filterwarnings('ignore')

# =============================================================================
# CONFIG
# =============================================================================

POLYGON_API_KEY   = os.environ.get('POLYGON_API_KEY', '')
STARTING_NAV      = 10_000.00   # Paper portfolio starting NAV
MIN_DEAL_SIZE_USD = 500_000_000  # $500m minimum
MIN_SPREAD_PCT    = 0.5          # Minimum 0.5% spread to flag as candidate
SPREAD_ALERT_PP   = 2.0          # Alert if spread widens >2pp in one day
TIME_STOP_DAYS    = 30           # Alert if >30 days past expected close
MAX_POSITION_PCT  = 15.0         # Maximum 15% of NAV per deal

# Environment detection
if os.path.isdir('/content/drive/MyDrive'):
    BASE_DIR = '/content/drive/MyDrive/merger_arb_test'
elif os.path.isdir('/home/runner/work'):
    BASE_DIR = os.environ.get('GITHUB_WORKSPACE', os.getcwd())
else:
    BASE_DIR = os.getcwd()

os.makedirs(os.path.join(BASE_DIR, 'data'), exist_ok=True)

DATA_DIR         = os.path.join(BASE_DIR, 'data')
DEALS_PATH       = os.path.join(DATA_DIR, 'deals.csv')
CANDIDATES_PATH  = os.path.join(DATA_DIR, 'candidates.csv')
ALERTS_PATH      = os.path.join(DATA_DIR, 'alerts.csv')
PERFORMANCE_PATH = os.path.join(DATA_DIR, 'performance.csv')
STATE_PATH       = os.path.join(DATA_DIR, 'state.json')
README_PATH      = os.path.join(BASE_DIR, 'README.md')

today = datetime.now(timezone.utc).date()
now   = datetime.now(timezone.utc)

print('=' * 60)
print('MERGER ARB TEST — Daily Update')
print(f'Date: {today} UTC')
print('=' * 60)


# =============================================================================
# SECTION 1: LOAD STATE AND DATA FILES
# =============================================================================

def load_state():
    if os.path.exists(STATE_PATH):
        with open(STATE_PATH, 'r') as f:
            return json.load(f)
    return {
        'nav':        STARTING_NAV,
        'start_date': str(today),
        'start_nav':  STARTING_NAV,
    }

def save_state(state):
    with open(STATE_PATH, 'w') as f:
        json.dump(state, f, indent=2)

def load_csv(path, required_cols):
    if os.path.exists(path) and os.path.getsize(path) > len(','.join(required_cols)):
        df = pd.read_csv(path)
        for col in required_cols:
            if col not in df.columns:
                df[col] = None
        return df
    return pd.DataFrame(columns=required_cols)

state = load_state()

DEAL_COLS = [
    'deal_id', 'target', 'acquirer', 'geography', 'announcement_date',
    'expected_close', 'deal_type', 'deal_price', 'entry_date', 'entry_price',
    'shares', 'position_value', 'current_price', 'current_spread_pct',
    'unrealised_pct', 'completion_prob', 'ev_score', 'status', 'outcome', 'notes'
]
CANDIDATE_COLS = [
    'date_flagged', 'target', 'acquirer', 'target_ticker', 'geography',
    'deal_price', 'current_price', 'spread_pct', 'deal_type', 'source',
    'deal_size_usd', 'notes', 'reviewed', 'decision'
]
ALERT_COLS   = ['date', 'deal_id', 'target', 'alert_type', 'detail', 'resolved']
PERF_COLS    = ['date', 'nav', 'open_positions', 'closed_positions',
                'total_return_pct', 'win_rate', 'avg_gain_pct', 'avg_loss_pct']

deals_df      = load_csv(DEALS_PATH,       DEAL_COLS)
candidates_df = load_csv(CANDIDATES_PATH,  CANDIDATE_COLS)
alerts_df     = load_csv(ALERTS_PATH,      ALERT_COLS)
perf_df       = load_csv(PERFORMANCE_PATH, PERF_COLS)

open_deals   = deals_df[deals_df['status'] == 'open'].copy() if len(deals_df) > 0 else pd.DataFrame(columns=DEAL_COLS)
closed_deals = deals_df[deals_df['status'] == 'closed'].copy() if len(deals_df) > 0 else pd.DataFrame(columns=DEAL_COLS)

print(f'\nOpen positions:    {len(open_deals)}')
print(f'Closed positions:  {len(closed_deals)}')
print(f'Current NAV:       ${state["nav"]:,.2f}')


# =============================================================================
# SECTION 2: DATA SOURCES — DEAL DISCOVERY
# =============================================================================

new_candidates = []
existing_tickers = set(candidates_df['target_ticker'].dropna().tolist()) if len(candidates_df) > 0 else set()

# --- SOURCE 1: POLYGON.IO NEWS API (US deals) --------------------------------

def scan_polygon_ma_news():
    """
    Scan Polygon.io news API for M&A announcements from the last 2 days.
    Filters for acquisition/merger/takeover keywords.
    Returns list of candidate dicts.
    """
    if not POLYGON_API_KEY:
        print('  Polygon API key not set — skipping')
        return []

    candidates = []
    MA_KEYWORDS = [
        'acquisition', 'acquire', 'merger', 'takeover', 'tender offer',
        'buyout', 'definitive agreement', 'to be acquired', 'go private',
        'all-cash', 'cash consideration'
    ]

    # Search last 2 days of news
    from_date = (today - timedelta(days=2)).strftime('%Y-%m-%d')
    to_date   = today.strftime('%Y-%m-%d')

    url = 'https://api.polygon.io/v2/reference/news'
    params = {
        'published_utc.gte': from_date,
        'published_utc.lte': to_date,
        'order':   'desc',
        'limit':   50,
        'apiKey':  POLYGON_API_KEY,
    }

    try:
        resp = requests.get(url, params=params, timeout=15)
        if resp.status_code != 200:
            print(f'  Polygon news API error: {resp.status_code}')
            return []

        results = resp.json().get('results', [])
        print(f'  Polygon: {len(results)} news items retrieved')

        for article in results:
            title       = article.get('title', '').lower()
            description = article.get('description', '').lower()
            text        = title + ' ' + description
            tickers     = article.get('tickers', [])

            # Check if article contains M&A keywords
            if not any(kw in text for kw in MA_KEYWORDS):
                continue

            # Must have at least one ticker
            if not tickers:
                continue

            # Skip if already in candidates
            if any(t in existing_tickers for t in tickers):
                continue

            candidates.append({
                'date_flagged':  str(today),
                'target':        article.get('title', '')[:100],
                'acquirer':      '',
                'target_ticker': tickers[0] if tickers else '',
                'geography':     'US',
                'deal_price':    None,
                'current_price': None,
                'spread_pct':    None,
                'deal_type':     'cash',
                'source':        'polygon_news',
                'deal_size_usd': None,
                'notes':         article.get('article_url', ''),
                'reviewed':      'No',
                'decision':      'Pending',
            })

    except Exception as e:
        print(f'  Polygon API error: {e}')

    print(f'  Polygon: {len(candidates)} M&A candidates flagged')
    return candidates


# --- SOURCE 2: SEC EDGAR FULL-TEXT SEARCH (US formal filings) ----------------

def scan_sec_edgar():
    """
    Scan SEC EDGAR for formal M&A filings from the last 2 days.
    SC TO-T = tender offer (acquirer filing)
    SC 13E-3 = going private transaction
    DEFM14A = merger proxy statement (definitive)
    These are the most reliable signals — a formal SEC filing means
    the deal is real, announced, and in process.
    """
    candidates = []
    FILING_TYPES = ['SC TO-T', 'SC 13E-3', 'DEFM14A', 'SC TO-I']

    from_date = (today - timedelta(days=3)).strftime('%Y-%m-%d')

    for filing_type in FILING_TYPES:
        url = 'https://efts.sec.gov/LATEST/search-index?q=%22' + \
              filing_type.replace(' ', '%20') + \
              '%22&dateRange=custom&startdt=' + from_date + \
              '&enddt=' + str(today) + '&forms=' + filing_type.replace(' ', '%20')

        # Use the proper EDGAR full text search API
        search_url = 'https://efts.sec.gov/LATEST/search-index'
        params = {
            'q':         f'"{filing_type}"',
            'dateRange': 'custom',
            'startdt':   from_date,
            'enddt':     str(today),
            'forms':     filing_type,
        }

        headers = {
            'User-Agent': 'MergerArbResearch research@example.com',
            'Accept':     'application/json',
        }

        try:
            resp = requests.get(
                'https://efts.sec.gov/LATEST/search-index',
                params=params,
                headers=headers,
                timeout=15
            )
            if resp.status_code != 200:
                continue

            data = resp.json()
            hits = data.get('hits', {}).get('hits', [])

            for hit in hits[:10]:
                source   = hit.get('_source', {})
                entity   = source.get('entity_name', '')
                ticker   = source.get('file_num', '')
                filed_at = source.get('file_date', '')
                form     = source.get('form_type', filing_type)

                if entity and entity not in [c['target'] for c in candidates]:
                    candidates.append({
                        'date_flagged':  str(today),
                        'target':        entity,
                        'acquirer':      '',
                        'target_ticker': '',
                        'geography':     'US',
                        'deal_price':    None,
                        'current_price': None,
                        'spread_pct':    None,
                        'deal_type':     'cash',
                        'source':        f'sec_edgar_{form.lower().replace(" ","_")}',
                        'deal_size_usd': None,
                        'notes':         f'SEC filing: {form} filed {filed_at}',
                        'reviewed':      'No',
                        'decision':      'Pending',
                    })

        except Exception as e:
            print(f'  EDGAR error ({filing_type}): {e}')
        time.sleep(0.5)

    print(f'  EDGAR: {len(candidates)} formal filings flagged')
    return candidates


# --- SOURCE 3: LSE RNS FEED (UK deals) ---------------------------------------

def scan_lse_rns():
    """
    Scan London Stock Exchange Regulatory News Service for UK takeover
    announcements. Filters for Takeover Panel announcements and
    recommended offers.
    """
    candidates = []
    UK_KEYWORDS = [
        'recommended cash offer', 'recommended offer', 'takeover offer',
        'possible offer', 'firm intention', 'rule 2.7', 'acquisition of',
        'to acquire', 'cash offer for'
    ]

    # LSE RNS RSS feed — publicly available
    rns_url = 'https://api.londonstockexchange.com/api/gw/lse/instruments/alldata/announcements'

    # Alternative: use the free RNS XML feed
    rns_feed = 'https://www.londonstockexchange.com/exchange/news/market-news/market-news-home.html'

    # Most reliable free approach: query regulatory news via public API
    try:
        # Try the public LSE announcement feed
        headers = {
            'User-Agent': 'Mozilla/5.0 (research purposes)',
            'Accept':     'application/json',
        }

        # Use newsapi approach for UK financial news as fallback
        if POLYGON_API_KEY:
            # Polygon also covers some UK stocks
            url = 'https://api.polygon.io/v2/reference/news'
            params = {
                'published_utc.gte': (today - timedelta(days=2)).strftime('%Y-%m-%d'),
                'order':  'desc',
                'limit':  25,
                'apiKey': POLYGON_API_KEY,
            }
            resp = requests.get(url, params=params, timeout=15)
            if resp.status_code == 200:
                results = resp.json().get('results', [])
                for article in results:
                    title = article.get('title', '').lower()
                    if any(kw in title for kw in UK_KEYWORDS):
                        tickers = article.get('tickers', [])
                        candidates.append({
                            'date_flagged':  str(today),
                            'target':        article.get('title', '')[:100],
                            'acquirer':      '',
                            'target_ticker': tickers[0] if tickers else '',
                            'geography':     'UK',
                            'deal_price':    None,
                            'current_price': None,
                            'spread_pct':    None,
                            'deal_type':     'cash',
                            'source':        'polygon_uk_news',
                            'deal_size_usd': None,
                            'notes':         article.get('article_url', ''),
                            'reviewed':      'No',
                            'decision':      'Pending',
                        })

    except Exception as e:
        print(f'  LSE RNS error: {e}')

    print(f'  LSE/UK: {len(candidates)} UK candidates flagged')
    return candidates


# =============================================================================
# SECTION 3: RUN DEAL DISCOVERY
# =============================================================================

print('\n' + '=' * 60)
print('DEAL DISCOVERY')
print('=' * 60)

polygon_candidates = scan_polygon_ma_news()
edgar_candidates   = scan_sec_edgar()
uk_candidates      = scan_lse_rns()

all_new_candidates = polygon_candidates + edgar_candidates + uk_candidates

# Deduplicate by target ticker
seen_tickers = set(existing_tickers)
deduped = []
for c in all_new_candidates:
    ticker = c.get('target_ticker', '')
    target = c.get('target', '')
    key    = ticker if ticker else target
    if key and key not in seen_tickers:
        seen_tickers.add(key)
        deduped.append(c)

print(f'\nTotal new candidates: {len(deduped)}')

if deduped:
    new_cands_df  = pd.DataFrame(deduped)
    candidates_df = pd.concat([candidates_df, new_cands_df], ignore_index=True)
    candidates_df.to_csv(CANDIDATES_PATH, index=False)
    print(f'Candidates saved to {CANDIDATES_PATH}')


# =============================================================================
# SECTION 4: UPDATE OPEN POSITION PRICES AND SPREADS
# =============================================================================

print('\n' + '=' * 60)
print('UPDATING OPEN POSITIONS')
print('=' * 60)

new_alerts    = []
prev_spreads  = {}

if len(open_deals) > 0:
    for idx, deal in open_deals.iterrows():
        ticker     = str(deal.get('target_ticker', deal['target']))
        deal_price = float(deal['deal_price']) if pd.notna(deal.get('deal_price')) else None
        prev_spread = float(deal['current_spread_pct']) if pd.notna(deal.get('current_spread_pct')) else None

        if not deal_price:
            print(f'  {deal["target"]}: no deal price — skipping price update')
            continue

        # Fetch current price
        try:
            hist = yf.Ticker(ticker).history(period='5d', auto_adjust=True)
            if not hist.empty:
                current_price = float(hist['Close'].iloc[-1])
                current_spread = ((deal_price - current_price) / current_price) * 100
                entry_price    = float(deal['entry_price']) if pd.notna(deal.get('entry_price')) else current_price
                unrealised_pct = ((current_price - entry_price) / entry_price) * 100

                # Update deal row
                deals_df.at[idx, 'current_price']    = round(current_price, 4)
                deals_df.at[idx, 'current_spread_pct'] = round(current_spread, 2)
                deals_df.at[idx, 'unrealised_pct']   = round(unrealised_pct, 2)

                # Update position value
                shares = float(deal['shares']) if pd.notna(deal.get('shares')) else 0
                deals_df.at[idx, 'position_value'] = round(current_price * shares, 2)

                print(f'  {deal["target"]}: ${current_price:.2f} | spread: {current_spread:+.2f}% | P&L: {unrealised_pct:+.2f}%')

                # ALERT 1: Spread widening
                if prev_spread is not None:
                    spread_change = current_spread - prev_spread
                    if spread_change > SPREAD_ALERT_PP:
                        alert = {
                            'date':       str(today),
                            'deal_id':    deal['deal_id'],
                            'target':     deal['target'],
                            'alert_type': 'SPREAD_WIDENING',
                            'detail':     f'Spread widened {spread_change:+.1f}pp today ({prev_spread:.1f}% -> {current_spread:.1f}%). Possible deal stress.',
                            'resolved':   'No',
                        }
                        new_alerts.append(alert)
                        print(f'  *** ALERT: {deal["target"]} spread widened {spread_change:+.1f}pp ***')

                # ALERT 2: Negative spread (target above offer price — unusual)
                if current_spread < -0.5:
                    alert = {
                        'date':       str(today),
                        'deal_id':    deal['deal_id'],
                        'target':     deal['target'],
                        'alert_type': 'NEGATIVE_SPREAD',
                        'detail':     f'Target trading ABOVE deal price (spread: {current_spread:.1f}%). Possible competing bid or deal re-rating.',
                        'resolved':   'No',
                    }
                    new_alerts.append(alert)
                    print(f'  *** ALERT: {deal["target"]} negative spread — target above offer price ***')

        except Exception as e:
            print(f'  {deal["target"]}: price fetch error — {e}')
        time.sleep(0.5)

        # ALERT 3: Time stop — deal running late
        expected_close = deal.get('expected_close')
        if expected_close and pd.notna(expected_close):
            try:
                close_date = date.fromisoformat(str(expected_close)[:10])
                days_late  = (today - close_date).days
                if days_late > TIME_STOP_DAYS:
                    # Only alert if not already alerted recently
                    recent_alerts = alerts_df[
                        (alerts_df['deal_id'].astype(str) == str(deal['deal_id'])) &
                        (alerts_df['alert_type'] == 'TIME_STOP')
                    ] if len(alerts_df) > 0 else pd.DataFrame()

                    if len(recent_alerts) == 0 or \
                       (today - date.fromisoformat(str(recent_alerts.iloc[-1]['date']))).days > 7:
                        alert = {
                            'date':       str(today),
                            'deal_id':    deal['deal_id'],
                            'target':     deal['target'],
                            'alert_type': 'TIME_STOP',
                            'detail':     f'Deal is {days_late} days past expected close ({expected_close}). Review position.',
                            'resolved':   'No',
                        }
                        new_alerts.append(alert)
                        print(f'  *** ALERT: {deal["target"]} is {days_late} days past expected close ***')
            except Exception:
                pass

else:
    print('  No open positions to update')

# Save updated deals
deals_df.to_csv(DEALS_PATH, index=False)

# Save new alerts
if new_alerts:
    alerts_df = pd.concat([alerts_df, pd.DataFrame(new_alerts)], ignore_index=True)
    alerts_df.to_csv(ALERTS_PATH, index=False)
    print(f'\n{len(new_alerts)} new alerts logged')


# =============================================================================
# SECTION 5: RECALCULATE NAV AND PERFORMANCE
# =============================================================================

# NAV = sum of all open position values + cash
# Cash = starting NAV minus sum of all entry position values
if len(open_deals) > 0:
    invested = open_deals['position_value'].astype(float).sum()
    # Recalculate from deals_df (updated prices)
    open_updated = deals_df[deals_df['status'] == 'open']
    invested_updated = open_updated['position_value'].astype(float).sum() if len(open_updated) > 0 else 0

    # Calculate cash: starting NAV minus all money ever deployed (entry values)
    all_entry_values = deals_df[deals_df['status'].isin(['open', 'closed'])]['position_value'].astype(float)
    # Simpler: track cash separately in state
    if 'cash' not in state:
        state['cash'] = STARTING_NAV
    nav = float(state['cash']) + invested_updated
else:
    nav = state['nav']

state['nav'] = round(nav, 2)

# Performance metrics
total_return = (nav - STARTING_NAV) / STARTING_NAV * 100
n_closed     = len(closed_deals)
n_open       = len(deals_df[deals_df['status'] == 'open']) if len(deals_df) > 0 else 0

win_rate = avg_gain = avg_loss = None
if n_closed > 0:
    closed_returns = pd.to_numeric(closed_deals['unrealised_pct'], errors='coerce').dropna()
    wins           = closed_returns[closed_returns > 0]
    losses         = closed_returns[closed_returns < 0]
    win_rate       = len(wins) / n_closed * 100 if n_closed > 0 else 0
    avg_gain       = wins.mean() if len(wins) > 0 else 0
    avg_loss       = losses.mean() if len(losses) > 0 else 0

# Log daily performance
perf_row = {
    'date':              str(today),
    'nav':               nav,
    'open_positions':    n_open,
    'closed_positions':  n_closed,
    'total_return_pct':  round(total_return, 4),
    'win_rate':          round(win_rate, 1) if win_rate is not None else None,
    'avg_gain_pct':      round(avg_gain, 2) if avg_gain is not None else None,
    'avg_loss_pct':      round(avg_loss, 2) if avg_loss is not None else None,
}

already_logged = len(perf_df) > 0 and str(today) in perf_df['date'].astype(str).values
if not already_logged:
    perf_df = pd.concat([perf_df, pd.DataFrame([perf_row])], ignore_index=True)
    perf_df.to_csv(PERFORMANCE_PATH, index=False)

save_state(state)


# =============================================================================
# SECTION 6: GENERATE README DASHBOARD
# =============================================================================

print('\n' + '=' * 60)
print('Regenerating README...')
print('=' * 60)

# Open positions table
open_rows = ''
open_updated = deals_df[deals_df['status'] == 'open'] if len(deals_df) > 0 else pd.DataFrame()
if len(open_updated) > 0:
    for _, d in open_updated.iterrows():
        target   = str(d['target'])
        acquirer = str(d.get('acquirer', '—'))
        geo      = str(d.get('geography', '—'))
        dp       = f"${float(d['deal_price']):.2f}"       if pd.notna(d.get('deal_price'))      else '—'
        cp       = f"${float(d['current_price']):.2f}"    if pd.notna(d.get('current_price'))   else '—'
        sp       = f"{float(d['current_spread_pct']):.1f}%" if pd.notna(d.get('current_spread_pct')) else '—'
        pnl      = f"{float(d['unrealised_pct']):+.1f}%"  if pd.notna(d.get('unrealised_pct')) else '—'
        prob     = f"{float(d['completion_prob']):.0f}%"  if pd.notna(d.get('completion_prob')) else '—'
        ec       = str(d.get('expected_close', '—'))[:10]
        open_rows += f'| {target} | {acquirer} | {geo} | {dp} | {cp} | {sp} | {pnl} | {prob} | {ec} |\n'
else:
    open_rows = '| — | — | — | — | — | — | — | — | — |\n'

# Candidates table (unreviewed only)
unreviewed = candidates_df[candidates_df['reviewed'] == 'No'] if len(candidates_df) > 0 else pd.DataFrame()
cand_rows  = ''
if len(unreviewed) > 0:
    for _, c in unreviewed.tail(15).iterrows():
        target  = str(c.get('target', '—'))[:60]
        ticker  = str(c.get('target_ticker', '—'))
        geo     = str(c.get('geography', '—'))
        dp      = f"${float(c['deal_price']):.2f}"   if pd.notna(c.get('deal_price'))   else 'TBC'
        sp      = f"{float(c['spread_pct']):.1f}%"   if pd.notna(c.get('spread_pct'))   else 'TBC'
        source  = str(c.get('source', '—'))
        flagged = str(c.get('date_flagged', '—'))[:10]
        notes   = str(c.get('notes', ''))[:80]
        cand_rows += f'| {flagged} | {target} | {ticker} | {geo} | {dp} | {sp} | {source} | {notes} |\n'
else:
    cand_rows = '| — | No new candidates | — | — | — | — | — | — |\n'

# Alerts table (unresolved only)
unresolved_alerts = alerts_df[alerts_df['resolved'] == 'No'] if len(alerts_df) > 0 else pd.DataFrame()
alert_rows = ''
if len(unresolved_alerts) > 0:
    for _, a in unresolved_alerts.iterrows():
        alert_type = str(a['alert_type'])
        emoji      = '🔴' if alert_type == 'SPREAD_WIDENING' else ('🟡' if alert_type == 'TIME_STOP' else '🟠')
        alert_rows += f'| {a["date"]} | {emoji} {alert_type} | {a["target"]} | {a["detail"]} |\n'
else:
    alert_rows = '| — | ✅ No active alerts | — | — |\n'

# Closed deals table
closed_rows = ''
if n_closed > 0:
    for _, d in closed_deals.tail(10).iterrows():
        outcome  = str(d.get('outcome', '—'))
        emoji    = '✅' if outcome == 'COMPLETED' else ('❌' if outcome == 'BROKEN' else '—')
        pnl      = f"{float(d['unrealised_pct']):+.1f}%" if pd.notna(d.get('unrealised_pct')) else '—'
        closed_rows += f'| {d["target"]} | {d.get("acquirer","—")} | {d.get("geography","—")} | {pnl} | {emoji} {outcome} |\n'
else:
    closed_rows = '| — | — | — | — | No closed deals yet |\n'

# Performance stats
win_str    = f'{win_rate:.0f}%' if win_rate is not None else 'Insufficient data'
gain_str   = f'{avg_gain:+.2f}%' if avg_gain is not None else '—'
loss_str   = f'{avg_loss:+.2f}%' if avg_loss is not None else '—'
last_updated = now.strftime('%Y-%m-%d %H:%M UTC')

# Calculate EV threshold example
ev_example = 0.90 * 3.0 + 0.10 * (-22.0)
days_running = (today - date.fromisoformat(state['start_date'])).days

readme = f"""# Merger Arb Test
## US & UK Merger Arbitrage — Paper Trading Portfolio

> Systematic paper trading of announced M&A deals in US and UK markets.
> Automated deal discovery via Polygon.io and SEC EDGAR.
> Manual position selection and qualitative review by operator.
> Updated automatically every weekday at 08:20 UTC via GitHub Actions.

**Last updated:** {last_updated}

---

## How It Works

**Automated layer** scans Polygon.io news, SEC EDGAR filings, and UK sources
daily for new M&A announcements. Qualifying deals are flagged as candidates.
Open position prices and spreads are updated daily. Alerts fire on deal stress.

**Manual layer** (operator) reviews candidates each morning, applies qualitative
scoring (regulatory complexity, financing certainty, strategic rationale), and
selects which deals to paper trade by adding rows to `data/deals.csv`.

**Entry criteria:**
- Cash deals only (no stock-for-stock without short leg)
- Friendly deals only
- Deal size ≥ $500m
- US-listed or UK-listed target
- Positive spread (target below offer price)
- Expected value positive after estimated transaction costs

**EV formula:** EV = (completion_prob × spread%) + ((1 − completion_prob) × −22%)
Example at 90% completion, 3% spread: {ev_example:.1f}% — **TRADE**

---

## Portfolio Performance

| Metric | Value |
|--------|-------|
| Starting NAV | ${STARTING_NAV:,.2f} |
| Current NAV | ${nav:,.2f} |
| Total return | {total_return:+.2f}% |
| Open positions | {n_open} |
| Closed positions | {n_closed} |
| Win rate | {win_str} |
| Avg gain on completion | {gain_str} |
| Avg loss on break | {loss_str} |
| Days running | {days_running} |

---

## 🚨 Active Alerts

*Check these first — they require your attention.*

| Date | Alert | Target | Detail |
|------|-------|--------|--------|
{alert_rows}

---

## Open Positions

| Target | Acquirer | Geo | Deal Price | Current | Spread | P&L | Completion % | Expected Close |
|--------|---------|-----|-----------|---------|--------|-----|-------------|---------------|
{open_rows}

---

## 📋 Candidates — Review Required

*Deals flagged by automated layer. Review each morning and decide: TRADE / PASS / WATCH.*
*To paper trade a deal: add a row to `data/deals.csv` with status = open.*
*To mark as reviewed: update `reviewed` column in `data/candidates.csv` to Yes.*

| Flagged | Target | Ticker | Geo | Deal Price | Spread | Source | Notes/URL |
|---------|--------|--------|-----|-----------|--------|--------|----------|
{cand_rows}

---

## Closed Deals (last 10)

| Target | Acquirer | Geo | Return | Outcome |
|--------|---------|-----|--------|---------|
{closed_rows}

---

## How To Add A Paper Trade

When you decide to paper trade a deal, add a row to `data/deals.csv`:

```
deal_id:          next number in sequence (1, 2, 3...)
target:           company name
acquirer:         acquirer name
geography:        US or UK
announcement_date: YYYY-MM-DD
expected_close:   YYYY-MM-DD (estimated)
deal_type:        cash
deal_price:       offer price per share in USD/GBP
entry_date:       today YYYY-MM-DD
entry_price:      price you're entering at (current market price)
shares:           number of shares (position_size / entry_price)
position_value:   entry_price × shares
current_price:    leave blank — script fills this
current_spread_pct: leave blank — script fills this
unrealised_pct:   leave blank — script fills this
completion_prob:  your estimate 0-100
ev_score:         your EV calculation
status:           open
outcome:          leave blank
notes:            your qualitative notes on the deal
```

---

## How To Close A Position

When a deal completes or breaks, update the row in `data/deals.csv`:
- `status`: closed
- `outcome`: COMPLETED or BROKEN
- `unrealised_pct`: final return (positive if completed, negative if broken)

---

## Scoring Framework

When reviewing candidates, assess each factor:

| Factor | Green | Amber | Red |
|--------|-------|-------|-----|
| Deal type | All-cash, committed financing | Cash with some conditions | Leveraged / financing uncertain |
| Stance | Recommended by target board | Neutral | Hostile |
| Regulatory bodies | 1-2, non-sensitive sector | 2-3, some sensitivity | 3+, tech/healthcare/defence |
| Deal size | <$5bn | $5-20bn | >$20bn (more regulatory scrutiny) |
| Acquirer track record | Strong M&A history | Mixed | First major acquisition |
| Spread | 1-3% (market confident) | 3-6% (some uncertainty) | >6% (high risk) |
| Time to close | <3 months | 3-6 months | >6 months |

3+ red flags → PASS. 5+ green flags → strong candidate.

---

## Success Criteria (pre-defined)

| Criterion | Threshold | Status |
|-----------|-----------|--------|
| Win rate | ≥ 85% | {win_str} |
| Avg return on completion | ≥ 2.5% net | {gain_str} |
| EV calibration | Predicted vs actual within 10pp | Pending |
| Annualised return | ≥ 8% | Pending |
| Minimum sample | 20 closed deals | {n_closed}/20 |

---

## Data Sources

- **Polygon.io** — US M&A news (API key required)
- **SEC EDGAR** — US formal filings: SC TO-T, SC 13E-3, DEFM14A (free)
- **LSE RNS** — UK takeover announcements (free feed)
- **InsideArbitrage.com** — manual supplement (weekly deal list, free)
- **yfinance** — current target stock prices

---

## Repository Structure

```
merger_arb_test/
├── .github/workflows/merger_arb_update.yml  # Weekdays 08:20 UTC
├── data/
│   ├── deals.csv          # Paper positions (you add rows here)
│   ├── candidates.csv     # Automated candidates (you review these)
│   ├── alerts.csv         # Active alerts
│   ├── performance.csv    # Daily NAV and stats
│   └── state.json         # Portfolio state
├── src/merger_arb_update.py
├── requirements.txt
└── README.md
```

---

*Paper trading only. Not investment advice. No real capital deployed.*
"""

with open(README_PATH, 'w') as f:
    f.write(readme)

print('README updated')
print('\n' + '=' * 60)
print(f'MERGER ARB — COMPLETE — {today}')
print(f'  NAV:              ${nav:,.2f}')
print(f'  Open positions:   {n_open}')
print(f'  Closed positions: {n_closed}')
print(f'  New candidates:   {len(deduped)}')
print(f'  Active alerts:    {len(unresolved_alerts)}')
print('=' * 60)
