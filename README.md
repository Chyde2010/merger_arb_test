# Merger Arb Test
## US & UK Merger Arbitrage — Paper Trading Portfolio

> Systematic paper trading of announced M&A deals in US and UK markets.
> Automated deal discovery via Polygon.io and SEC EDGAR.
> Manual position selection and qualitative review by operator.
> Updated automatically every weekday at 08:20 UTC via GitHub Actions.

**Last updated:** 2026-08-07 06:43 UTC

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
| Current NAV | $10,130.70 |
| Total return | +1.31% |
| Open positions | 9 |
| Closed positions | 0 |
| Win rate | Insufficient data |
| Avg gain on completion | — |
| Avg loss on break | — |
| Days running | 26 |

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
| Spire Healthcare Group | Toscafund Asset Management | UK | p250.00 | p233.50 | 7.1% | +8.1% | 72% | 2026-11-30 |
| Tate & Lyle PLC | Ingredion Incorporated | UK | p615.00 | p554.00 | 11.0% | -1.2% | 88% | 2026-10-31 |
| Beazley PLC | Zurich Insurance Group | UK | p1310.00 | p1290.50 | 1.5% | +0.3% | 96% | 2026-10-31 |
| Intertek Group PLC | EQT AB (Isotope Bidco) | UK | p6000.00 | p5840.00 | 2.7% | +4.0% | 85% | 2027-01-31 |
| Rotork PLC | ABB Ltd | UK | p506.00 | p486.20 | 4.1% | +0.2% | 91% | 2027-03-31 |
| easyJet PLC | Apollo Global Management | UK | p715.00 | p630.00 | 13.5% | -6.7% | 82% | 2027-02-28 |
| Ramsdens Holdings PLC | FirstCash Holdings Inc | UK | p675.00 | p666.00 | 1.4% | — | 97% | 2026-11-30 |
| DCC PLC | KKR & Co / Energy Capital Partners | UK | p6797.00 | p6330.00 | 7.4% | +2.5% | 76% | 2027-03-31 |
| Capricorn Energy PLC | Genel Energy No.9 Limited | UK | p357.00 | p366.00 | -2.5% | +6.1% | 92% | 2026-10-31 |


---

## 📋 Candidates — Review Required

*Deals flagged by automated layer. Review each morning and decide: TRADE / PASS / WATCH.*
*To paper trade a deal: add a row to `data/deals.csv` with status = open.*
*To mark as reviewed: update `reviewed` column in `data/candidates.csv` to Yes.*

| Flagged | Target | Ticker | Geo | Deal Price | Spread | Source | Notes/URL |
|---------|--------|--------|-----|-----------|--------|--------|----------|
| 2026-08-02 | Scripps completes acquisition of WTVQ in Lexington | SSP | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/08/01/3337133/0/en/Scripps-compl |
| 2026-08-03 | Share repurchase programme: Transactions of week 31 2026 | JYSKY | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/08/03/3337214/0/en/Share-repurch |
| 2026-08-03 | SoundHound AI's Next Earnings Report on Aug. 5 Could Send th | SOUN | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/08/02/soundhound-ais-next-earnings-report-on |
| 2026-08-04 | Why Atkore Stock Soared Today | ATKR | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/08/03/why-atkore-stock-soared-today/?source= |
| 2026-08-06 | H1 2026: Record order intake for RENK with above-average inc | RKGRY | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/08/06/3339931/0/en/H1-2026-Recor |
| 2026-08-06 | red violet Announces Pricing of $100 Million Underwritten Pu | RDVT | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/08/06/3339902/0/en/red-violet-An |
| 2026-08-06 | Gran Tierra Energy (GTE) Q2 2026 Earnings Call | GTE | US | TBC | TBC | polygon_news | https://www.fool.com/earnings/call-transcripts/2026/08/05/gran-tierra-energy-gte |
| 2026-08-07 | TPC Group to Be Acquired by ENEOS Holdings | JXHLY | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/08/07/3340914/15270/en/tpc-group |
| 2026-08-07 | SpaceX and Tesla Merger Talks Are Heating Up. Here's Why Inv | SPCX | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/08/06/spacex-and-tesla-merger-talks-are-heat |
| 2026-08-07 | ROSEN, A TOP-RANKED LAW FIRM, Encourages GPGI, Inc. f/k/a Co | GPGI | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/08/07/3340898/673/en/rosen-a-top |
| 2026-08-07 | ROSEN, TOP RANKED GLOBAL COUNSEL, Encourages DNOW Inc. Inves | DNOW | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/08/06/3340881/673/en/ROSEN-TOP-R |
| 2026-08-07 | Why Joby Aviation Stock Flew Higher Today | JOBY | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/08/06/why-joby-aviation-stock-flew-higher-to |
| 2026-08-07 | Biogen Completes Acquisition of RayThera Inc. | BIIB | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/08/06/3340877/0/en/Biogen-Comple |
| 2026-08-07 | Is Cactus Stock Still a Buy After a Board Member Shed 10,000 | WHD | US | TBC | TBC | polygon_news | https://www.fool.com/coverage/filings/2026/08/06/is-cactus-stock-still-a-buy-aft |
| 2026-08-07 | Why SiTime Stock Blasted Almost 27% Higher on Thursday | SITM | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/08/06/why-sitime-stock-blasted-almost-27-hig |


---

## Closed Deals (last 10)

| Target | Acquirer | Geo | Return | Outcome |
|--------|---------|-----|--------|---------|
| — | — | — | — | No closed deals yet |


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
| Win rate | ≥ 85% | Insufficient data |
| Avg return on completion | ≥ 2.5% net | — |
| EV calibration | Predicted vs actual within 10pp | Pending |
| Annualised return | ≥ 8% | Pending |
| Minimum sample | 20 closed deals | 0/20 |

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
