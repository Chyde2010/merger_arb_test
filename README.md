# Merger Arb Test
## US & UK Merger Arbitrage — Paper Trading Portfolio

> Systematic paper trading of announced M&A deals in US and UK markets.
> Automated deal discovery via Polygon.io and SEC EDGAR.
> Manual position selection and qualitative review by operator.
> Updated automatically every weekday at 08:20 UTC via GitHub Actions.

**Last updated:** 2026-10-26 11:20 UTC

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
Example at 90% completion, 3% spread: 0.5% — **TRADE**

---

## Portfolio Performance

| Metric | Value |
|--------|-------|
| Starting NAV | $10,000.00 |
| Current NAV | $10,235.12 |
| Total return | +2.35% |
| Open positions | 8 |
| Closed positions | 1 |
| Win rate | 0% |
| Avg gain on completion | +0.00% |
| Avg loss on break | -1.43% |
| Days running | 106 |

---

## 🚨 Active Alerts

*Check these first — they require your attention.*

| Date | Alert | Target | Detail |
|------|-------|--------|--------|
| 2026-07-16 | 🟠 NEGATIVE_SPREAD | Spire Healthcare Group | Target trading ABOVE deal price (spread: -98.9%). Possible competing bid or deal re-rating. |
| 2026-07-16 | 🟠 NEGATIVE_SPREAD | Tate & Lyle PLC | Target trading ABOVE deal price (spread: -98.9%). Possible competing bid or deal re-rating. |
| 2026-07-16 | 🟠 NEGATIVE_SPREAD | Beazley PLC | Target trading ABOVE deal price (spread: -99.0%). Possible competing bid or deal re-rating. |
| 2026-07-16 | 🟠 NEGATIVE_SPREAD | Intertek Group PLC | Target trading ABOVE deal price (spread: -99.0%). Possible competing bid or deal re-rating. |
| 2026-07-16 | 🔴 SPREAD_WIDENING | Spire Healthcare Group | Spread widened +14.9pp today (0.0% -> 14.9%). Possible deal stress. |
| 2026-07-16 | 🔴 SPREAD_WIDENING | Tate & Lyle PLC | Spread widened +9.9pp today (0.0% -> 9.9%). Possible deal stress. |
| 2026-07-16 | 🔴 SPREAD_WIDENING | Intertek Group PLC | Spread widened +3.1pp today (0.0% -> 3.1%). Possible deal stress. |
| 2026-07-16 | 🟠 NEGATIVE_SPREAD | Spire Healthcare Group | Target trading ABOVE deal price (spread: -98.9%). Possible competing bid or deal re-rating. |
| 2026-07-16 | 🟠 NEGATIVE_SPREAD | Tate & Lyle PLC | Target trading ABOVE deal price (spread: -98.9%). Possible competing bid or deal re-rating. |
| 2026-07-16 | 🟠 NEGATIVE_SPREAD | Beazley PLC | Target trading ABOVE deal price (spread: -99.0%). Possible competing bid or deal re-rating. |
| 2026-07-16 | 🟠 NEGATIVE_SPREAD | Intertek Group PLC | Target trading ABOVE deal price (spread: -99.0%). Possible competing bid or deal re-rating. |
| 2026-07-16 | 🟠 NEGATIVE_SPREAD | Spire Healthcare Group | Target trading ABOVE deal price (spread: -98.9%). Possible competing bid or deal re-rating. |
| 2026-07-16 | 🟠 NEGATIVE_SPREAD | Tate & Lyle PLC | Target trading ABOVE deal price (spread: -98.9%). Possible competing bid or deal re-rating. |
| 2026-07-16 | 🟠 NEGATIVE_SPREAD | Beazley PLC | Target trading ABOVE deal price (spread: -99.0%). Possible competing bid or deal re-rating. |
| 2026-07-16 | 🟠 NEGATIVE_SPREAD | Intertek Group PLC | Target trading ABOVE deal price (spread: -99.0%). Possible competing bid or deal re-rating. |
| 2026-07-16 | 🔴 SPREAD_WIDENING | Spire Healthcare Group | Spread widened +14.7pp today (0.0% -> 14.7%). Possible deal stress. |
| 2026-07-16 | 🔴 SPREAD_WIDENING | Tate & Lyle PLC | Spread widened +9.9pp today (0.0% -> 9.9%). Possible deal stress. |
| 2026-07-16 | 🔴 SPREAD_WIDENING | Intertek Group PLC | Spread widened +3.0pp today (0.0% -> 3.0%). Possible deal stress. |
| 2026-07-22 | 🔴 SPREAD_WIDENING | Spire Healthcare Group | Spread widened +11035.9pp today (0.0% -> 11035.9%). Possible deal stress. |
| 2026-07-22 | 🔴 SPREAD_WIDENING | Tate & Lyle PLC | Spread widened +10882.9pp today (0.0% -> 10882.9%). Possible deal stress. |
| 2026-07-22 | 🔴 SPREAD_WIDENING | Beazley PLC | Spread widened +10066.9pp today (0.0% -> 10066.9%). Possible deal stress. |
| 2026-07-22 | 🔴 SPREAD_WIDENING | Intertek Group PLC | Spread widened +10209.3pp today (0.0% -> 10209.3%). Possible deal stress. |
| 2026-07-22 | 🔴 SPREAD_WIDENING | Rotork PLC | Spread widened +10328.7pp today (0.0% -> 10328.7%). Possible deal stress. |
| 2026-07-22 | 🔴 SPREAD_WIDENING | easyJet PLC | Spread widened +10694.1pp today (0.0% -> 10694.1%). Possible deal stress. |
| 2026-07-22 | 🔴 SPREAD_WIDENING | Ramsdens Holdings PLC | Spread widened +10046.6pp today (0.0% -> 10046.6%). Possible deal stress. |
| 2026-07-22 | 🔴 SPREAD_WIDENING | Spire Healthcare Group | Spread widened +24.9pp today (11035.9% -> 11060.7%). Possible deal stress. |
| 2026-07-22 | 🔴 SPREAD_WIDENING | Ramsdens Holdings PLC | Spread widened +19.1pp today (10046.6% -> 10065.7%). Possible deal stress. |
| 2026-07-22 | 🔴 SPREAD_WIDENING | DCC PLC | Spread widened +7.7pp today (0.0% -> 7.7%). Possible deal stress. |


---

## Open Positions

| Target | Acquirer | Geo | Deal Price | Current | Spread | P&L | Completion % | Expected Close |
|--------|---------|-----|-----------|---------|--------|-----|-------------|---------------|
| Spire Healthcare Group | Toscafund Asset Management | UK | p250.00 | p234.00 | 6.8% | +8.3% | 72% | 2026-11-30 |
| Beazley PLC | Zurich Insurance Group | UK | p1310.00 | p1290.50 | 1.5% | +0.3% | 96% | 2026-10-31 |
| Intertek Group PLC | EQT AB (Isotope Bidco) | UK | p6000.00 | p5840.00 | 2.7% | +4.0% | 95% | 2027-01-31 |
| Rotork PLC | ABB Ltd | UK | p506.00 | p487.00 | 3.9% | +0.4% | 91% | 2027-03-31 |
| easyJet PLC | Castlelake LP | UK | p690.00 | p671.00 | 2.8% | -0.6% | 88% | 2027-02-28 |
| Ramsdens Holdings PLC | FirstCash Holdings Inc | UK | p675.00 | p664.00 | 1.7% | -0.3% | 97% | 2026-11-30 |
| DCC PLC | KKR & Co / Energy Capital Partners | UK | p6797.00 | p6375.00 | 6.6% | +3.2% | 80% | 2027-03-31 |
| Capricorn Energy PLC | Genel Energy No.9 Limited | UK | p381.00 | p374.00 | 1.9% | +8.4% | 92% | 2026-10-31 |


---

## 📋 Candidates — Review Required

*Deals flagged by automated layer. Review each morning and decide: TRADE / PASS / WATCH.*
*To paper trade a deal: add a row to `data/deals.csv` with status = open.*
*To mark as reviewed: update `reviewed` column in `data/candidates.csv` to Yes.*

| Flagged | Target | Ticker | Geo | Deal Price | Spread | Source | Notes/URL |
|---------|--------|--------|-----|-----------|--------|--------|----------|
| 2026-10-15 | Compass Lexecon Continues to Expand Competition Expertise Wi | FCN | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/10/15/3381306/33891/en/compass-l |
| 2026-10-16 | Director/PDMR Shareholding | AMIGY | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/10/16/3382255/0/en/director-pdmr |
| 2026-10-16 | Massive News for IonQ Stock Investors | IONQ | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/10/16/massive-news-for-ionq-stock-investors/ |
| 2026-10-16 | Strive Announces Pricing of Upsized Initial Public Offering  | ASST | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/10/16/3382236/0/en/strive-announ |
| 2026-10-16 | COMP Class Action Reminder – Robbins LLP Reminds Investors o | COMP | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/10/15/3382215/32719/en/comp-clas |
| 2026-10-19 | Red Cat Announces Proposed Voluntary Public Purchase Offer f | RCAT | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/10/19/3382970/0/en/red-cat-annou |
| 2026-10-21 | Comcast Trades at 6 Times Earnings and Yields 6%. Does It De | CCZ | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/10/21/comcast-earnings-yields-cheap-dividend |
| 2026-10-21 | Will Tesla’s New Flying Roadster Send the Stock Flying? | TSLA | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/10/21/will-tesla-s-new-flying-roadster-send- |
| 2026-10-21 | SIKA TO ACQUIRE ADHESIVES BUSINESS SERVING ASIAN GROWTH MARK | SXYAY | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/10/21/3385097/0/en/sika-to-acqui |
| 2026-10-23 | Why TTM Technologies Stock Plunged This Week | TTMI | US | TBC | TBC | polygon_news | https://www.fool.com/coverage/market-movers/2026/10/23/why-ttm-technologies-stoc |
| 2026-10-23 | Meta Is Doing Something It’s Never Done Before. Here’s What  | META | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/10/23/meta-is-doing-something-it-s-never-don |
| 2026-10-23 | Allegion: 3 Key Takeaways for Long-Term Investors | ALLE | US | TBC | TBC | polygon_news | https://www.fool.com/earnings/takeaways/2026/10/23/allegion-3-key-takeaways-for- |
| 2026-10-26 | Corxel US and Amanat Acquisition Corp Announce Definitive Bu | AMAN | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/10/26/3387902/0/en/corxel-us-and |
| 2026-10-26 | $CDNL Stock Losses: BFA Law Reminds Cardinal Infrastructure  | CDNL | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/10/26/3387899/0/en/cdnl-stock-lo |
| 2026-10-26 | STMicroelectronics introduces first automotive safety combin | STM | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/10/26/3387826/0/en/stmicroelectr |


---

## Closed Deals (last 10)

| Target | Acquirer | Geo | Return | Outcome |
|--------|---------|-----|--------|---------|
| Tate & Lyle PLC | Ingredion Incorporated | UK | -1.4% | — VOLUNTARY_EXIT |


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
| Win rate | ≥ 85% | 0% |
| Avg return on completion | ≥ 2.5% net | +0.00% |
| EV calibration | Predicted vs actual within 10pp | Pending |
| Annualised return | ≥ 8% | Pending |
| Minimum sample | 20 closed deals | 1/20 |

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
