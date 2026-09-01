# Merger Arb Test
## US & UK Merger Arbitrage — Paper Trading Portfolio

> Systematic paper trading of announced M&A deals in US and UK markets.
> Automated deal discovery via Polygon.io and SEC EDGAR.
> Manual position selection and qualitative review by operator.
> Updated automatically every weekday at 08:20 UTC via GitHub Actions.

**Last updated:** 2026-09-01 10:17 UTC

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
| Days running | 51 |

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
| 2026-08-19 | IZEA (IZEA) Q2 2026 Earnings Call Transcript | IZEA | US | TBC | TBC | polygon_news | https://www.fool.com/earnings/call-transcripts/2026/08/18/izea-izea-q2-2026-earn |
| 2026-08-19 | This Company Just Hit 50 Straight Years of Dividend Increase | CSL | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/08/18/this-company-just-hit-50-straight-year |
| 2026-08-20 | The Crowd Is Selling Campbell's Stock. Here's Why It's a Buy | CPB | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/08/19/the-crowd-is-selling-campbells-stock-h |
| 2026-08-21 | Interactive Brokers' Margin Loans Grew 49% in a Year to $100 | IBKR | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/08/20/interactive-brokers-margin-loans-grew- |
| 2026-08-21 | Why ScanSource Stock Is Soaring Today | SCSC | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/08/20/why-scansource-stock-is-soaring-today/ |
| 2026-08-25 | ExxonMobil Is Eyeing a Potential $8 Billion Bet on Shell's U | SHEL | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/08/24/exxonmobil-is-eyeing-an-8-billion-bet- |
| 2026-08-26 | Simply Good Foods Company Securities Fraud Class Action Resu | SMPL | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/08/26/3351060/6713/en/simply-goo |
| 2026-08-26 | Why Navitas Semiconductor Stock Is Up Today | NVTS | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/08/25/why-navitas-semiconductor-stock-is-up- |
| 2026-08-26 | UWM Holdings Corporation (UWMC) Investors with $150K+ Losses | UWMC | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/08/25/3351027/32716/en/uwm-holdi |
| 2026-08-27 | Here's Why Ensign Group Stock Remains a Buy for Investors | ENSG | US | TBC | TBC | polygon_news | https://www.zacks.com/stock/news/2981058/here-s-why-ensign-group-stock-remains-a |
| 2026-08-31 | VisionWave Holdings Provides Update on Pending Acquisition o | VWAV | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/08/31/3353159/0/en/visionwave-ho |
| 2026-09-01 | New Engen Named to ADWEEK’s Fastest Growing Agencies for Fou | UBER | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/09/01/3353897/0/en/new-engen-nam |
| 2026-09-01 | Should You Avoid Opendoor Stock, Even at a 52-Week Low? | OPEN | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/09/01/should-you-avoid-opendoor-stock-52-wee |
| 2026-09-01 | Can't Decide Between Investing in Rare-Earth Materials and N | UUUU | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/09/01/cant-decide-between-investing-in-rare- |
| 2026-09-01 | ROSEN, RECOGNIZED INVESTOR COUNSEL, Encourages DNOW Inc. Inv | DNOW | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/08/31/3353758/673/en/rosen-recog |


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
