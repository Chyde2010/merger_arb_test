# Merger Arb Test
## US & UK Merger Arbitrage — Paper Trading Portfolio

> Systematic paper trading of announced M&A deals in US and UK markets.
> Automated deal discovery via Polygon.io and SEC EDGAR.
> Manual position selection and qualitative review by operator.
> Updated automatically every weekday at 08:20 UTC via GitHub Actions.

**Last updated:** 2026-07-13 06:12 UTC

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
| Current NAV | $10,000.00 |
| Total return | +0.00% |
| Open positions | 0 |
| Closed positions | 0 |
| Win rate | Insufficient data |
| Avg gain on completion | — |
| Avg loss on break | — |
| Days running | 1 |

---

## 🚨 Active Alerts

*Check these first — they require your attention.*

| Date | Alert | Target | Detail |
|------|-------|--------|--------|
| — | ✅ No active alerts | — | — |


---

## Open Positions

| Target | Acquirer | Geo | Deal Price | Current | Spread | P&L | Completion % | Expected Close |
|--------|---------|-----|-----------|---------|--------|-----|-------------|---------------|
| — | — | — | — | — | — | — | — | — |


---

## 📋 Candidates — Review Required

*Deals flagged by automated layer. Review each morning and decide: TRADE / PASS / WATCH.*
*To paper trade a deal: add a row to `data/deals.csv` with status = open.*
*To mark as reviewed: update `reviewed` column in `data/candidates.csv` to Yes.*

| Flagged | Target | Ticker | Geo | Deal Price | Spread | Source | Notes/URL |
|---------|--------|--------|-----|-----------|--------|--------|----------|
| 2026-07-12 | Capital One Flips Millions of Discover Cards to Its Own Plat | COF | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/07/12/capital-one-flips-millions-of-discover |
| 2026-07-12 | 3 Dividend Stocks Worth Holding for the Long Haul | ET | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/07/12/3-dividend-stocks-worth-holding-for-th |
| 2026-07-12 | Netflix Might Be Ready to Buy Something Again, but It's Not  | NFLX | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/07/12/netflix-might-be-ready-to-buy-somethin |
| 2026-07-12 | ROSEN, TOP RANKED GLOBAL COUNSEL, Encourages GeneDx Holdings | WGS | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/11/3325828/673/en/ROSEN-TOP-R |
| 2026-07-13 | J.P. Morgan Called a Potential Elon Musk SpaceX-Tesla Merger | SPCX | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/07/12/jpmorgan-called-a-potential-elon-musk- |
| 2026-07-13 | This Looks Like the Perfect Stock for Warren Buffett and Gre | BRK.A | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/07/12/this-looks-like-the-perfect-stock-for- |


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
