# Merger Arb Test
## US & UK Merger Arbitrage — Paper Trading Portfolio

> Systematic paper trading of announced M&A deals in US and UK markets.
> Automated deal discovery via Polygon.io and SEC EDGAR.
> Manual position selection and qualitative review by operator.
> Updated automatically every weekday at 08:20 UTC via GitHub Actions.

**Last updated:** 2026-07-23 07:55 UTC

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
| Current NAV | $9,945.78 |
| Total return | -0.54% |
| Open positions | 9 |
| Closed positions | 0 |
| Win rate | Insufficient data |
| Avg gain on completion | — |
| Avg loss on break | — |
| Days running | 11 |

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
| Spire Healthcare Group | Toscafund Asset Management | UK | p250.00 | p222.00 | 12.6% | +2.8% | 72% | 2026-11-30 |
| Tate & Lyle PLC | Ingredion Incorporated | UK | p615.00 | p559.00 | 10.0% | -0.4% | 88% | 2026-10-31 |
| Beazley PLC | Zurich Insurance Group | UK | p1310.00 | p1288.00 | 1.7% | +0.1% | 96% | 2026-10-31 |
| Intertek Group PLC | EQT AB (Isotope Bidco) | UK | p6000.00 | p5820.00 | 3.1% | +3.6% | 85% | 2027-01-31 |
| Rotork PLC | ABB Ltd | UK | p506.00 | p485.00 | 4.3% | — | 91% | 2027-03-31 |
| easyJet PLC | Apollo Global Management | UK | p715.00 | p585.00 | 22.2% | -13.3% | 82% | 2027-02-28 |
| Ramsdens Holdings PLC | FirstCash Holdings Inc | UK | p675.00 | p666.00 | 1.4% | — | 97% | 2026-11-30 |
| DCC PLC | KKR & Co / Energy Capital Partners | UK | p6797.00 | p6295.00 | 8.0% | +1.9% | 76% | 2027-03-31 |
| Capricorn Energy PLC | Genel Energy No.9 Limited | UK | p357.00 | — | — | — | 92% | 2026-10-31 |


---

## 📋 Candidates — Review Required

*Deals flagged by automated layer. Review each morning and decide: TRADE / PASS / WATCH.*
*To paper trade a deal: add a row to `data/deals.csv` with status = open.*
*To mark as reviewed: update `reviewed` column in `data/candidates.csv` to Yes.*

| Flagged | Target | Ticker | Geo | Deal Price | Spread | Source | Notes/URL |
|---------|--------|--------|-----|-----------|--------|--------|----------|
| 2026-07-20 | Should You Buy Rocket Lab Stock Below $70? | RKLB | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/07/20/should-you-buy-rocket-lab-stock-below- |
| 2026-07-20 | Distribution Solutions Group Announces Controller Buyout; Ju | DSGR | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/20/3330065/0/en/Distribution- |
| 2026-07-20 | PERSONALIS SHAREHOLDER ALERT: PSNL Shareholders Interested i | PSNL | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/20/3329936/0/en/PERSONALIS-SH |
| 2026-07-21 | What This Paychex Insider Filing Signals as the Company Push | PAYX | US | TBC | TBC | polygon_news | https://www.fool.com/coverage/filings/2026/07/20/what-this-paychex-insider-filin |
| 2026-07-21 | What This Burke & Herbert Filing Signals With the Stock Up 1 | BHRB | US | TBC | TBC | polygon_news | https://www.fool.com/coverage/filings/2026/07/20/what-this-burke-and-herbert-fil |
| 2026-07-21 | What This Heritage Financial Insider Move Signals With the S | HFWA | US | TBC | TBC | polygon_news | https://www.fool.com/coverage/filings/2026/07/20/heritage-financial-cio-sells-33 |
| 2026-07-22 | GeneDx Holdings Securities Fraud Class Action Result of Acqu | WGS | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/22/3331055/6713/en/GeneDx-Hol |
| 2026-07-22 | 3 Reasons to Buy AbbVie Stock Like There's No Tomorrow | ABBV | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/07/21/3-reasons-to-buy-abbvie-stock-like-the |
| 2026-07-23 | Dassault Systèmes acquiert ArisGlobal pour créer une platefo | DASTY | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/23/3331852/0/fr/Dassault-Syst |
| 2026-07-23 | Motorsport Games Adopts Limited Duration Stockholder Rights  | MSGM | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/23/3331833/0/en/Motorsport-Ga |
| 2026-07-23 | TWG Announces Entry into of a Material Definitive Agreement  | TWG | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/23/3331830/0/en/TWG-Announces |
| 2026-07-23 | Union Pacific et le CN concluent une entente visant à élargi | UNP | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/23/3331823/0/fr/Union-Pacific |
| 2026-07-23 | Michelin: Disclosure of trading in own shares - July 23rd, 2 | MGDDY | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/23/3331890/0/en/Michelin-Disc |
| 2026-07-23 | ROSEN, TOP RANKED GLOBAL COUNSEL, Encourages GPGI, Inc. f/k/ | GPGI | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/23/3331824/673/en/ROSEN-TOP-R |
| 2026-07-23 | Northrim BanCorp, Inc. Signs Definitive Agreement to Acquire | NRIM | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/07/22/3331817/8875/en/Northrim-B |


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
