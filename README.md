# Merger Arb Test
## US & UK Merger Arbitrage — Paper Trading Portfolio

> Systematic paper trading of announced M&A deals in US and UK markets.
> Automated deal discovery via Polygon.io and SEC EDGAR.
> Manual position selection and qualitative review by operator.
> Updated automatically every weekday at 08:20 UTC via GitHub Actions.

**Last updated:** 2026-11-25 15:52 UTC

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
| Days running | 136 |

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
| 2026-11-12 | Katapult Holdings Reports Third Quarter 2026 Results | KPLT | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/11/12/3401326/0/en/katapult-hold |
| 2026-11-13 | Grupo Aval: 3 Key Takeaways for Long-Term Investors | AVAL | US | TBC | TBC | polygon_news | https://www.fool.com/earnings/takeaways/2026/11/13/grupo-aval-3-key-takeaways-fo |
| 2026-11-16 | Jasper Therapeutics Reports Third Quarter 2026 Financial Res | JSPR | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/11/16/3403434/0/en/jasper-therap |
| 2026-11-16 | Déclaration hebdomadaire des transactions sur CCI du 2026 11 | CRARY | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/11/16/3403246/0/fr/d%C3%A9clarat |
| 2026-11-17 | Cerrado Gold Announces Release Date for Third Quarter Financ | PAAS | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/11/17/3404384/0/en/cerrado-gold- |
| 2026-11-18 | CoinShares Announces Third Quarter 2026 Results | CSHR | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/11/18/3405457/0/en/coinshares-an |
| 2026-11-19 | Chemomab Therapeutics Announces Third Quarter 2026 Financial | CMMB | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/11/19/3406497/0/en/chemomab-ther |
| 2026-11-19 | ZenaTech Announces More than C$20 Million in Contracted Reve | ZENA | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/11/19/3406498/0/en/zenatech-anno |
| 2026-11-23 | Century Communities: 3 Key Takeaways for Long-Term Investors | CCS | US | TBC | TBC | polygon_news | https://www.fool.com/earnings/takeaways/2026/11/23/century-communities-3-key-tak |
| 2026-11-23 | Levenza launches personal AI agents globally for the enterpr | MSFT | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/11/23/3408386/0/en/levenza-launc |
| 2026-11-23 | Win Systems’ Casino Management Software Acquired by Volaris  | CNSWY | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/11/23/3408267/0/en/win-systems-c |
| 2026-11-25 | Kirby McInerney LLP Alerts Investors Who Acquired O-I Glass, | OI | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/11/25/3410335/937/en/kirby-mcine |
| 2026-11-25 | XRP Just Dropped Below $1. Here's the Contrarian Case for Bu | XRPC | US | TBC | TBC | polygon_news | https://www.fool.com/investing/2026/11/25/xrp-just-dropped-below-1-heres-the-con |
| 2026-11-25 | Coupang vs. Home Depot: Which Consumer Stock Is a Better Buy | CPNG | US | TBC | TBC | polygon_news | https://www.fool.com/coverage/better-buy/2026/11/25/coupang-vs-home-depot-which- |
| 2026-11-25 | Blue Gold Signs Non-Binding LOI to Acquire Established Londo | BGL | US | TBC | TBC | polygon_news | https://www.globenewswire.com/news-release/2026/11/25/3410119/0/en/blue-gold-sig |


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
