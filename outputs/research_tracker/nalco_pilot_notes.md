# NALCO Pilot Notes

## Company

National Aluminium Company Ltd (NATIONALUM.NS)

## Role in Pilot

NALCO is the second pilot company because it is a cash-rich public-sector commodity/metals company. It is useful for testing whether public provider enterprise value (EV) properly reflects large cash-like assets, bank balances, current investments, and limited borrowings.

Unlike BEL, which currently appears to behave like a clean reliability benchmark, NALCO is expected to be a more sensitive EV bridge case because commodity companies are often valued using EV-based multiples and because net cash can materially affect operating-business valuation.

## Why NALCO Belongs in the Pilot

NALCO satisfies the pilot selection criteria:

- Non-financial Indian listed company.
- EV/EBITDA and EV/Sales are relevant for commodity-cycle valuation.
- Public provider coverage is available.
- Annual-report cash, bank balances, investments, and borrowings can be note-locked.
- Balance-sheet structure is materially cash-rich.
- PSU/commodity status creates a different test case from BEL, Polycab, and Hero MotoCorp.

## Provider Snapshot

### Screener.in

Two Screener observations are currently documented.

#### Observation 1

- Public provider page date shown in captured result: 2026-04-10
- Current price shown: INR 417
- Market capitalization: INR 76,578 crore
- Provider EV: not visible in captured result
- Status: market capitalization captured; provider EV pending manual verification

#### Observation 2

- Public provider page date shown in captured result: 2026-05-07 close price
- Current price shown: INR 404
- Balance-sheet data visible through March 2026
- Borrowings shown for March 2025: INR 182 crore
- Borrowings shown for March 2026: INR 60 crore
- Investments shown for March 2025: INR 774 crore
- Investments shown for March 2026: INR 533 crore
- Provider EV: not visible in captured result
- Status: useful for provider balance-sheet cross-check; EV pending manual verification

### StockAnalysis

Two StockAnalysis observations are currently available from public search results:

#### Observation 1

- Page: NSE:NATIONALUM Statistics
- Provider date shown: 2026-03-12
- Market capitalization: INR 751.46 billion, approximately INR 75,146 crore
- Enterprise value: INR 672.96 billion, approximately INR 67,296 crore

#### Observation 2

- Page: NSE:NATIONALUM Market Cap
- Provider date shown: 2026-04-15
- Market capitalization: INR 778.55 billion, approximately INR 77,855 crore
- Enterprise value: INR 700.05 billion, approximately INR 70,005 crore

Because provider dates differ, these values should be treated as preliminary until a fixed-date provider snapshot is manually captured.

### Yahoo Finance

- Public Yahoo Finance page date shown in captured result: 2026-01-16
- Market capitalization: INR 663.94 billion, approximately INR 66,394 crore
- Enterprise value: INR 584.59 billion, approximately INR 58,459 crore
- EV / Revenue: 3.27
- EV / EBITDA: 6.54
- Total cash: INR 79.06 billion, approximately INR 7,906 crore
- Debt / Equity: 0.28%
- Status: provider EV and market cap captured, but date is older than StockAnalysis/Screener observations; treat as preliminary and not date-comparable.

### Moneycontrol

- Public Moneycontrol page date shown in captured result: 2026-05-07, 03:59
- Current price shown: INR 403.50
- Revenue shown for 2026: INR 17,843.05 crore
- Net profit shown for 2026: INR 5,815.76 crore
- Debt-to-equity shown for 2026: 0.00
- Provider EV: not visible in captured result
- Market capitalization: not visible in captured result
- Status: useful for financial cross-check; EV and market capitalization still pending manual capture.

## Prior Annual-Report Note-Lock Values

From the earlier Monte Carlo DCF project, the NALCO annual-report lock used:

- Cash and cash equivalents: INR 121.40 crore
- Bank balances other than cash and cash equivalents: INR 5,305.33 crore
- Current investments: INR 514.92 crore
- Current borrowings: INR 124.22 crore
- Cash-like assets: INR 5,941.65 crore
- Conservative net cash after current borrowings: INR 5,817.43 crore

## Preliminary Reconstructed EV

Using the conservative cash-like treatment:

```text
Reconstructed EV = Market Cap + Current Borrowings - Cash-like Assets
```

Equivalently:

```text
Reconstructed EV = Market Cap - Conservative Net Cash
```

### Screener market-cap basis, 2026-04-10 observation

```text
76,578.00 - 5,817.43 = 70,760.57 crore
```

### StockAnalysis 2026-03-12 market-cap basis

```text
75,146.00 - 5,817.43 = 69,328.57 crore
```

### StockAnalysis 2026-04-15 market-cap basis

```text
77,855.00 - 5,817.43 = 72,037.57 crore
```

### Yahoo Finance 2026-01-16 market-cap basis

```text
66,394.00 - 5,817.43 = 60,576.57 crore
```

## Preliminary Provider Deviation

### StockAnalysis Observation 1: 2026-03-12

```text
Provider EV = 67,296.00 crore
Reconstructed EV = 69,328.57 crore
Absolute deviation = -2,032.57 crore
Percentage deviation = -2.93%
```

### StockAnalysis Observation 2: 2026-04-15

```text
Provider EV = 70,005.00 crore
Reconstructed EV = 72,037.57 crore
Absolute deviation = -2,032.57 crore
Percentage deviation = -2.82%
```

### Yahoo Finance Observation: 2026-01-16

```text
Provider EV = 58,459.00 crore
Reconstructed EV = 60,576.57 crore
Absolute deviation = -2,117.57 crore
Percentage deviation = -3.50%
```

## Preliminary Interpretation

NALCO appears more interesting than BEL for the EV reconciliation pilot. The preliminary StockAnalysis observations imply a provider EV below the conservative reconstructed EV by approximately INR 2,033 crore, or around 2.8-2.9%. The preliminary Yahoo Finance observation implies a provider EV below the conservative reconstructed EV by approximately INR 2,118 crore, or around 3.5%.

This is not yet a high-deviation case, but it falls in the moderate 2-5% bucket. The likely research question is whether providers are subtracting a broader set of cash-like or financial assets than the conservative reconstruction, or whether timing and balance-sheet update differences explain the gap.

The result remains preliminary because provider dates differ and Moneycontrol/Screener EV values still require manual verification.

## Data Quality Status

Status: preliminary, needs review.

Completed items:

1. Captured preliminary StockAnalysis market cap and EV.
2. Captured preliminary Yahoo Finance market cap and EV.
3. Captured Screener market cap and balance-sheet cross-check items.
4. Captured Moneycontrol financial cross-check items.

Open items:

1. Capture fixed-date Moneycontrol market cap and EV if visible.
2. Capture Screener EV if visible or document if unavailable.
3. Re-verify NALCO annual-report page and note references.
4. Decide whether conservative cash-like treatment should include any broader financial assets.
5. Update the working CSV after all provider values are collected and date-aligned.
6. Do not treat current observations as final because provider dates are not fully aligned.

## Current Pilot Signal

BEL currently looks like a low-deviation reliability benchmark.

NALCO currently looks like a moderate-deviation cash-rich commodity case.

This supports the paper's framing: public provider EV may be reliable in some cases and moderately divergent in others depending on cash/investment treatment, provider timing, and balance-sheet complexity.
