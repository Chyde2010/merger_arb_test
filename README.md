# Merger Arb Test
## US & UK Merger Arbitrage — Paper Trading Portfolio

> Systematic paper trading of announced M&A deals in US and UK markets.
> Automated deal discovery via Polygon.io and SEC EDGAR.
> Manual position selection and qualitative review by operator.
> Updated automatically every weekday at 08:20 UTC via GitHub Actions.

**Last updated:** 2026-07-20 08:22 UTC

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
| Current NAV | $13,988.81 |
| Total return | +39.89% |
| Open positions | 4 |
| Closed positions | 0 |
| Win rate | Insufficient data |
| Avg gain on completion | — |
| Avg loss on break | — |
| Days running | 8 |

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


---

## Open Positions

| Target | Acquirer | Geo | Deal Price | Current | Spread | P&L | Completion % | Expected Close |
|--------|---------|-----|-----------|---------|--------|-----|-------------|---------------|
| Spire Healthcare Group | Toscafund Asset Management | UK | p2.50 | p2.19 | 14.2% | +1.4% | 72% | 2026-11-30 |
| Tate & Lyle PLC | Ingredion Incorporated | UK | p6.15 | p5.59 | 10.0% | -0.4% | 88% | 2026-10-31 |
| Beazley PLC | Zurich Insurance Group | UK | p13.10 | p12.88 | 1.7% | +0.1% | 96% | 2026-10-31 |
| Intertek Group PLC | EQT AB (Isotope Bidco) | UK | p60.00 | p58.25 | 3.0% | +3.7% | 85% | 2027-01-31 |


---

## 📋 Candidates — Review Required

*Deals flagged by automated layer. Review each morning and decide: TRADE / PASS / WATCH.*
*To paper trade a deal: add a row to `data/deals.csv` with status = open.*
*To mark as reviewed: update `reviewed` column in `data/candidates.csv` to Yes.*

| Flagged | Target | Ticker | Geo | Deal Price | Spread | Source | Notes/URL |
|---------|--------|--------|-----|-----------|--------|--------|----------|
| 2026-07-13 | 3 Dividend Stocks with Growth on Tap for the Second Half | IBM | US | TBC | TBC | polygon_news | https://www.investing.com/analysis/3-dividend-stocks-with-growth-on-tap-for-the- |
| 2026-07-14 | VEON and JazzWorld Acquire TPL Insurance to Expand Digital I | VEON | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/14/3326556/0/en/VEON-and-Jazz |
| 2026-07-15 | Closing of Previously Announced Restructuring Transaction in | RY | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/15/3327442/0/en/Closing-of-Pr |
| 2026-07-15 | Zillow Group Securities Fraud Class Action Arising from Alle | Z | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/15/3327440/6713/en/Zillow-Gro |
| 2026-07-15 | Cadence Design Systems vs. Synopsys: Which Technology Stock  | CDNS | US | TBC | TBC | polygon_news | https://www.fool.com/coverage/better-buy/2026/07/14/cadence-design-systems-vs-sy |
| 2026-07-16 | Stripe and Advent Reportedly Bid $60.50 a Share for PayPal.  | PYPL | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/07/15/stripe-and-advent-reportedly-bid-6050- |
| 2026-07-16 | Centerra Gold Announces Extension and Increase of its Corpor | CGAU | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/15/3328145/0/en/Centerra-Gold |
| 2026-07-16 | Angelini Pharma Completes Acquisition of Catalyst Pharmaceut | CPRX | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/16/3328252/0/en/Angelini-Phar |
| 2026-07-17 | Telia Lietuva results for 6 months of 2026 | TLSNY | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/17/3328903/0/en/Telia-Lietuva |
| 2026-07-17 | Marketing Veteran Bryan Dulaney is advising SafeSpace Global | SSGC | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/16/3328880/0/en/Marketing-Vet |
| 2026-07-17 | Why AtaiBeckley Stock Soared Today | ATAI | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/07/16/why-ataibeckley-stock-is-up-today/?sou |
| 2026-07-20 | Could Pfizer Ultimately Be the Biggest Winner in the $100 Bi | PFE | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/07/20/could-pfizer-ultimately-be-the-biggest |
| 2026-07-20 | Cribl acquiert CardinalOps pour étendre sa plateforme d'IA a | PANW | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/20/3329449/0/fr/Cribl-acquier |
| 2026-07-20 | EVA LIVE TARGETS A $3 TRILLION GLOBAL DEFENSE, SATELLITE AND | GOAI | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/20/3329416/0/en/EVA-LIVE-TARG |
| 2026-07-20 | ROSEN, A RANKED AND LEADING LAW FIRM, Encourages GPGI, Inc.  | GPGI | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/19/3329403/673/en/ROSEN-A-RAN |


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
