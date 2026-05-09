# BEL Pilot Notes

## Company

Bharat Electronics Ltd (BEL.NS)

## Role in Pilot

BEL is the first pilot company because it is a cash-rich defence electronics company with wide public-provider coverage and prior annual-report note-lock work from the earlier Monte Carlo DCF project.

BEL is not expected to produce a dramatic EV divergence by default. Its role is to act as a reliability benchmark: if provider EV is close to annual-report reconstructed EV for a large, liquid, widely covered company, that is still a useful finding.

## Current Provider Snapshot

### Screener.in

- Access date: 2026-05-10
- Provider date shown: 2026-05-07 close price
- Market capitalization: INR 321,265 crore
- Current price: INR 439
- Provider EV: not visible in the captured provider snapshot
- Status: market capitalization captured; EV pending manual verification

### StockAnalysis

- Access date: 2026-05-10
- Provider date shown: 2026-05-07
- Market capitalization: INR 3.21 trillion, approximately INR 321,000 crore
- Enterprise value: INR 3.13 trillion, approximately INR 313,000 crore
- EV / Sales: 11.81
- EV / EBITDA: 39.84
- Debt / Equity: 0.00
- Debt / EBITDA: 0.01
- Status: provider market cap and EV captured

### Yahoo Finance

- Status: pending manual capture

### Moneycontrol

- Status: pending manual capture

## Prior Annual-Report Note-Lock Values

From the earlier Monte Carlo DCF project, the BEL annual-report lock used:

- Cash and cash equivalents: INR 713.45 crore
- Bank balances other than cash and equivalents: INR 8,831.65 crore
- Borrowings: nil
- Conservative cash-like assets: INR 9,545.10 crore
- Broader financial assets including non-current investments: INR 10,126.71 crore

## Preliminary Reconstructed EV

Using the conservative cash-like treatment:

```text
Reconstructed EV = Market Cap - Conservative Cash-like Assets
```

### Screener market-cap basis

```text
321,265.00 - 9,545.10 = 311,719.90 crore
```

### StockAnalysis market-cap basis

```text
321,000.00 - 9,545.10 = 311,454.90 crore
```

## Preliminary StockAnalysis Deviation

Using the approximate StockAnalysis EV value:

```text
Provider EV = 313,000.00 crore
Reconstructed EV = 311,454.90 crore
Absolute deviation = 1,545.10 crore
Percentage deviation = 0.50%
```

## Preliminary Interpretation

BEL is currently a useful reliability benchmark. StockAnalysis reports EV of approximately INR 313,000 crore, while the preliminary reconstructed EV using the conservative cash-like treatment is approximately INR 311,454.90 crore on the StockAnalysis market-cap basis. The preliminary deviation is approximately 0.50%, which is below the 2% low-deviation threshold.

This does not weaken the paper. It helps define the reliability side of the research question: large, liquid, widely covered companies may have provider EV values close to annual-report reconstructed EV. The larger research value comes from comparing this clean benchmark with more complex companies such as NALCO, Polycab, Hero MotoCorp, and later the expanded 30-50 company sample.

## Data Quality Status

Status: preliminary, needs review.

Open items:

1. Capture Yahoo Finance EV and market capitalization.
2. Capture Moneycontrol EV and market capitalization.
3. Re-verify BEL annual-report page and note references.
4. Decide whether to disclose non-current investments separately or include them in broader financial assets.
5. Update the working CSV after all provider values are collected.
