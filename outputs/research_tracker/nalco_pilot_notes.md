# NALCO Pilot Notes

## Company

National Aluminium Company Ltd (NATIONALUM.NS)

## Role in Pilot

NALCO is the second pilot company because it is a cash-rich public-sector commodity/metals company. It is useful for testing whether public provider enterprise value (EV) properly reflects large cash-like assets, bank balances, current investments, lease liabilities, and limited borrowings.

Unlike BEL, which currently appears to behave like a clean reliability benchmark, NALCO is expected to be a more sensitive EV bridge case because commodity companies are often valued using EV-based multiples and because net cash can materially affect operating-business valuation.

## Why NALCO Belongs in the Pilot

NALCO satisfies the pilot selection criteria:

- Non-financial Indian listed company.
- EV/EBITDA and EV/Sales are relevant for commodity-cycle valuation.
- Public provider coverage is available.
- Annual-report cash, bank balances, investments, borrowings, and lease liabilities can be note-locked.
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
- Status: market capitalization captured; provider EV not visible in available capture.

#### Observation 2

- Public provider page date shown in captured result: 2026-05-07 close price
- Current price shown: INR 404
- Balance-sheet data visible through March 2026
- Borrowings shown for March 2025: INR 182 crore
- Borrowings shown for March 2026: INR 60 crore
- Investments shown for March 2025: INR 774 crore
- Investments shown for March 2026: INR 533 crore
- Provider EV: not visible in captured result
- Status: useful for provider balance-sheet cross-check; EV not visible in available capture.

### StockAnalysis

Three StockAnalysis observations are currently documented.

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

#### Observation 3

- Page: NSE:NATIONALUM Statistics
- Provider date shown: 2026-05-08
- Market capitalization: INR 741.08 billion, approximately INR 74,108 crore
- Enterprise value: INR 654.67 billion, approximately INR 65,467 crore
- Status: later StockAnalysis snapshot; still preliminary until fixed-date protocol is finalized.

Because provider dates differ, these values should be treated as preliminary until a fixed-date provider snapshot is manually captured.

### Yahoo Finance

- Public Yahoo Finance page date shown in captured result: around May 2026 / prior capture also noted 2026-01-16
- Market capitalization: approximately INR 74,209 crore from Perplexity source-discovery output; earlier captured observation showed approximately INR 66,394 crore
- Enterprise value: approximately INR 66,274 crore from Perplexity source-discovery output; earlier captured observation showed approximately INR 58,459 crore
- EV / Revenue: 3.27 in earlier captured observation
- EV / EBITDA: 6.54 in earlier captured observation
- Total cash: approximately INR 7,906 crore in earlier captured observation
- Debt / Equity: 0.28% in earlier captured observation
- Status: provider EV and market cap captured, but date alignment needs review.

### Moneycontrol

- Public Moneycontrol page date shown in captured result: 2026-05-07, 03:59
- Current price shown: INR 403.50
- Market capitalization from Perplexity source-discovery output: INR 73,823 crore
- Revenue shown for 2026: INR 17,843.05 crore
- Net profit shown for 2026: INR 5,815.76 crore
- Debt-to-equity shown for 2026: 0.00
- Current Moneycontrol provider EV: not visible in available current capture
- Historical Moneycontrol ratios page showed older EV values, including an Enterprise Value line of INR 26,939.71 crore in a historical ratios table. This is not comparable to the current May 2026 market-cap snapshot and should not be used as current provider EV.
- Status: current market capitalization useful; current EV remains not visible. Historical EV ratios page excluded from current deviation calculation.

## Provider Visibility Conclusion

For the current NALCO pilot stage:

| Provider | Market cap status | EV status | Use in deviation table? |
|---|---|---|---|
| StockAnalysis | Captured | Captured | Yes, preliminary |
| Yahoo Finance | Captured through source-discovery output | Captured through source-discovery output | Yes, preliminary with date-warning |
| Screener.in | Captured | Not visible in available capture | No, EV missing |
| Moneycontrol | Captured through source-discovery output | Not visible in current capture | No, EV missing |

## FY2024-25 Annual-Report Note-Lock Values

The FY2024-25 annual report balance sheet provides the audit-grade source for NALCO's EV bridge. The values below are extracted from the standalone balance sheet, page 154 / PDF page 156.

| Item | Value (INR crore) | Note | Treatment |
|---|---:|---|---|
| Current investments | 514.92 | Note 9 | Subtract if cash-like |
| Cash and cash equivalents | 121.40 | Note 16 | Subtract |
| Bank balances other than cash and equivalents | 5,305.33 | Note 16 | Subtract if cash-like |
| Current borrowings | 124.22 | Note 20 | Add |
| Non-current lease liabilities | 50.94 | Note 19 | Add if lease-adjusted EV is used |
| Current lease liabilities | 6.58 | Note 19 | Add if lease-adjusted EV is used |
| Non-current investments in joint ventures | 499.58 | Note 9 | Disclose separately; not automatically cash-like |
| Other non-current investments | 0.03 | Note 9 | Disclose separately; immaterial |

## Audit-Grade EV Bridge

### Conservative cash-like assets

```text
Cash-like assets = Cash and cash equivalents + Bank balances + Current investments
Cash-like assets = 121.40 + 5,305.33 + 514.92 = 5,941.65 crore
```

### Conservative net cash before lease adjustment

```text
Conservative net cash = Cash-like assets - Current borrowings
Conservative net cash = 5,941.65 - 124.22 = 5,817.43 crore
```

### Lease-adjusted net cash

```text
Total lease liabilities = 50.94 + 6.58 = 57.52 crore
Lease-adjusted net cash = 5,817.43 - 57.52 = 5,759.91 crore
```

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

### StockAnalysis 2026-05-08 market-cap basis

```text
74,108.00 - 5,817.43 = 68,290.57 crore
```

### Yahoo Finance approximate May 2026 market-cap basis

```text
74,209.00 - 5,817.43 = 68,391.57 crore
```

### Yahoo Finance earlier captured market-cap basis

```text
66,394.00 - 5,817.43 = 60,576.57 crore
```

### Moneycontrol market-cap basis

```text
73,823.00 - 5,817.43 = 68,005.57 crore
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

### StockAnalysis Observation 3: 2026-05-08

```text
Provider EV = 65,467.00 crore
Reconstructed EV = 68,290.57 crore
Absolute deviation = -2,823.57 crore
Percentage deviation = -4.13%
```

### Yahoo Finance approximate May 2026 observation

```text
Provider EV = 66,274.00 crore
Reconstructed EV = 68,391.57 crore
Absolute deviation = -2,117.57 crore
Percentage deviation = -3.10%
```

### Yahoo Finance earlier captured observation

```text
Provider EV = 58,459.00 crore
Reconstructed EV = 60,576.57 crore
Absolute deviation = -2,117.57 crore
Percentage deviation = -3.50%
```

## Preliminary Interpretation

NALCO appears more interesting than BEL for the EV reconciliation pilot. StockAnalysis and Yahoo Finance observations imply provider EV below conservative reconstructed EV by roughly 2.8% to 4.1%, depending on provider date and market-cap basis.

This is not yet a high-deviation case, but it consistently falls in the moderate 2-5% bucket for the provider EV values currently visible. The likely research question is whether providers are subtracting a broader set of cash-like or financial assets than the conservative reconstruction, whether they treat leases differently, or whether timing and balance-sheet update differences explain the gap.

Screener and Moneycontrol are currently useful for market-cap or financial cross-checks, but their current EV values are not visible in the available captures. They should therefore be excluded from NALCO provider-deviation calculations until manually verified.

## Data Quality Status

Status: annual-report note lock completed; provider date alignment still needs review.

Completed items:

1. Captured preliminary StockAnalysis market cap and EV.
2. Captured preliminary Yahoo Finance market cap and EV.
3. Captured Screener market cap and balance-sheet cross-check items.
4. Captured Moneycontrol financial cross-check items.
5. Uploaded FY2024-25 NALCO annual report.
6. Completed annual-report note lock for current investments, cash and cash equivalents, bank balances, borrowings, and lease liabilities.
7. Documented that current Screener EV is not visible in available capture.
8. Documented that current Moneycontrol EV is not visible in available capture; historical Moneycontrol EV ratios are excluded from current comparison.

Open items:

1. Verify whether provider EV values are lease-adjusted or non-lease-adjusted.
2. Update the working CSV after all provider values are collected and date-aligned.
3. Do not treat current observations as final because provider dates are not fully aligned.

## Current Pilot Signal

BEL currently looks like a low-deviation reliability benchmark.

NALCO currently looks like a moderate-deviation cash-rich commodity case.

This supports the paper's framing: public provider EV may be reliable in some cases and moderately divergent in others depending on cash/investment treatment, provider timing, lease treatment, and balance-sheet complexity.
