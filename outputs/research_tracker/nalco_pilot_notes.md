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

- Accessed/captured from public search result: 2026-05-10
- Provider page date shown in search result: 2026-04-10
- Current price shown: INR 417
- Market capitalization: INR 76,578 crore
- Provider EV: not visible in the captured search-result snapshot
- Status: market capitalization captured; provider EV pending manual verification

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

- Status: pending manual capture

### Moneycontrol

- Status: pending manual capture

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

### Screener market-cap basis

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

## Preliminary StockAnalysis Deviation

### Observation 1: 2026-03-12

```text
Provider EV = 67,296.00 crore
Reconstructed EV = 69,328.57 crore
Absolute deviation = -2,032.57 crore
Percentage deviation = -2.93%
```

### Observation 2: 2026-04-15

```text
Provider EV = 70,005.00 crore
Reconstructed EV = 72,037.57 crore
Absolute deviation = -2,032.57 crore
Percentage deviation = -2.82%
```

## Preliminary Interpretation

NALCO appears more interesting than BEL for the EV reconciliation pilot. The preliminary StockAnalysis observations imply a provider EV below the conservative reconstructed EV by approximately INR 2,033 crore, or around 2.8-2.9%.

This is not yet a high-deviation case, but it falls in the moderate 2-5% bucket. The likely research question is whether StockAnalysis is subtracting a broader set of cash-like or financial assets than the conservative reconstruction, or whether timing and balance-sheet update differences explain the gap.

The result remains preliminary because provider dates differ and Yahoo Finance, Moneycontrol, and Screener EV values still need manual capture.

## Data Quality Status

Status: preliminary, needs review.

Open items:

1. Capture fixed-date Yahoo Finance market cap and EV.
2. Capture fixed-date Moneycontrol market cap and EV.
3. Capture Screener EV if visible or document if unavailable.
4. Re-verify NALCO annual-report page and note references.
5. Decide whether the conservative cash-like treatment should include any broader financial assets.
6. Update the working CSV after all provider values are collected.

## Current Pilot Signal

BEL currently looks like a low-deviation reliability benchmark.

NALCO currently looks like a moderate-deviation cash-rich commodity case.

This supports the paper's framing: public provider EV may be reliable in some cases and moderately divergent in others depending on cash/investment treatment, provider timing, and balance-sheet complexity.
