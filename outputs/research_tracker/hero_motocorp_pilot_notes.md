# Hero MotoCorp Pilot Notes

## Company

Hero MotoCorp Ltd (HEROMOTOCO.NS)

## Role in Pilot

Hero MotoCorp is the fourth pilot company because it represents a mature, liquid, large-cap Indian operating business with strong public-provider coverage, substantial cash-like investments, low conventional borrowings, and meaningful lease liabilities. It functions as a control-style large-cap case, but with enough balance-sheet complexity to test whether provider EV consistently treats current investments, leases, minority interest, and cash-like balances.

## Why Hero MotoCorp Belongs in the Pilot

Hero MotoCorp satisfies the pilot selection criteria:

- Non-financial Indian listed company.
- EV/EBITDA and EV/Sales are relevant valuation metrics for the auto sector.
- Widely followed large-cap company with public provider coverage.
- Annual-report cash, bank balances, current investments, borrowings, lease liabilities, and non-controlling interest can be note-locked.
- Mature cash-flow business useful as a benchmark against BEL, NALCO, and Polycab.
- Prior Monte Carlo DCF work already used Hero MotoCorp as a valuation case, supporting research continuity.

## Business Context from FY2024-25 Annual Report

Hero MotoCorp reported FY2024-25 consolidated revenue from operations of INR 40,923.42 crore, EBITDA of INR 5,868 crore in the performance highlights, and PAT of INR 4,610 crore in the corporate overview. The company sold approximately 5.9 million units and remained the world's largest two-wheeler manufacturer by volume for the 24th consecutive year.

The annual report also highlights a strong balance sheet, low debt, and strategic investments in future mobility, including electric vehicles, premium motorcycles, and a INR 510 crore investment in Euler Motors.

## Provider Snapshot

### StockAnalysis

Two StockAnalysis observations are currently documented.

#### Observation 1: NSE statistics page

- Provider page date shown: 2026-04-16
- Market capitalization: INR 1.06 trillion, approximately INR 106,000 crore
- Enterprise value: INR 958.14 billion, approximately INR 95,814 crore
- EV / Sales: 2.16
- EV / EBITDA: 13.79
- Debt / Equity: 0.03
- Debt / EBITDA: 0.11
- Status: provider market cap and EV captured; preliminary.

#### Observation 2: NSE market-cap page

- Provider page date shown: 2026-03-25 / 2026-03-26
- Market capitalization: INR 1.06 trillion, approximately INR 106,000 crore
- Enterprise value: INR 959.36 billion, approximately INR 95,936 crore
- Status: provider market cap and EV captured; preliminary.

### Screener.in

- Status: pending direct capture.
- Expected use: market capitalization, borrowings, investments, and ratio cross-check.

### Yahoo Finance

- Status: pending direct capture.
- Search results did not provide a clean current Yahoo Finance market-cap and EV pair in INR crore.

### Moneycontrol

- Status: pending direct capture.
- Search results did not provide a clean current Moneycontrol market-cap and EV pair suitable for current deviation calculation.

## FY2024-25 Annual-Report Note-Lock Values

Hero MotoCorp's FY2024-25 annual report has been uploaded and note-locked. The consolidated balance sheet provides granular EV bridge items.

| Item | Value (INR crore) | Note | Treatment |
|---|---:|---|---|
| Current investments | 6,635.99 | Note 9B | Subtract if cash-like |
| Cash and cash equivalents | 383.55 | Note 16 | Subtract |
| Bank balances other than cash and cash equivalents | 190.53 | Note 17 | Subtract if cash-like |
| Current borrowings | 456.76 | Note 21 | Add |
| Non-current lease liabilities | 196.21 | Note 7 | Add in lease-adjusted EV |
| Current lease liabilities | 46.96 | Note 7 | Add in lease-adjusted EV |
| Non-controlling interests | 132.05 | Equity section / Note 20 | Add if minority-interest-adjusted EV is used |
| Non-current financial investments | 4,767.33 | Note 9B | Disclose separately; not automatically cash-like |
| Equity-accounted investments in associates | 2,980.94 | Note 9A | Disclose separately; not automatically cash-like |

## Annual-Report Evidence Notes

The consolidated balance sheet reports current investments of INR 6,635.99 crore, cash and cash equivalents of INR 383.55 crore, and bank balances other than cash and cash equivalents of INR 190.53 crore. It also reports current borrowings of INR 456.76 crore, current lease liabilities of INR 46.96 crore, non-current lease liabilities of INR 196.21 crore, and non-controlling interests of INR 132.05 crore.

The annual report also discloses non-current financial investments of INR 4,767.33 crore and equity-accounted investments in associates of INR 2,980.94 crore. These are important for analytical disclosure but are not automatically treated as cash-like in the base EV bridge.

## Audit-Grade EV Bridge

### Base cash-like assets

```text
Cash-like assets = Current investments + Cash and cash equivalents + Bank balances
Cash-like assets = 6,635.99 + 383.55 + 190.53 = 7,210.07 crore
```

### Gross borrowings

```text
Gross borrowings = Current borrowings
Gross borrowings = 456.76 crore
```

### Conservative net cash before lease and minority-interest adjustment

```text
Conservative net cash = Cash-like assets - Gross borrowings
Conservative net cash = 7,210.07 - 456.76 = 6,753.31 crore
```

### Lease-adjusted net cash

```text
Total lease liabilities = 196.21 + 46.96 = 243.17 crore
Lease-adjusted net cash = 6,753.31 - 243.17 = 6,510.14 crore
```

### Minority-interest-adjusted net cash equivalent

```text
Minority interest = 132.05 crore
Minority-interest-adjusted net cash = 6,753.31 - 132.05 = 6,621.26 crore
```

### Lease-and-minority-adjusted net cash equivalent

```text
Lease-and-minority-adjusted net cash = 6,753.31 - 243.17 - 132.05 = 6,378.09 crore
```

## Preliminary Reconstructed EV

### StockAnalysis market-cap basis, 2026-04-16 observation

Using conservative bridge with minority interest included:

```text
Market cap = 106,000.00 crore
Borrowings = 456.76 crore
Minority interest = 132.05 crore
Cash-like assets = 7,210.07 crore
Reconstructed EV = 106,000.00 + 456.76 + 132.05 - 7,210.07 = 99,378.74 crore
```

Using lease-and-minority-adjusted bridge:

```text
Market cap = 106,000.00 crore
Borrowings = 456.76 crore
Lease liabilities = 243.17 crore
Minority interest = 132.05 crore
Cash-like assets = 7,210.07 crore
Reconstructed EV = 106,000.00 + 456.76 + 243.17 + 132.05 - 7,210.07 = 99,621.91 crore
```

## Preliminary Provider Deviation

### StockAnalysis observation 1: 2026-04-16

Using conservative bridge with minority interest included:

```text
Provider EV = 95,814.00 crore
Reconstructed EV = 99,378.74 crore
Absolute deviation = -3,564.74 crore
Percentage deviation = -3.59%
```

Using lease-and-minority-adjusted bridge:

```text
Provider EV = 95,814.00 crore
Reconstructed EV = 99,621.91 crore
Absolute deviation = -3,807.91 crore
Percentage deviation = -3.82%
```

### StockAnalysis observation 2: 2026-03-26

Using conservative bridge with minority interest included:

```text
Provider EV = 95,936.00 crore
Reconstructed EV = 99,378.74 crore
Absolute deviation = -3,442.74 crore
Percentage deviation = -3.46%
```

Using lease-and-minority-adjusted bridge:

```text
Provider EV = 95,936.00 crore
Reconstructed EV = 99,621.91 crore
Absolute deviation = -3,685.91 crore
Percentage deviation = -3.70%
```

## Preliminary Interpretation

Hero MotoCorp currently looks like a moderate-deviation mature large-cap case. StockAnalysis EV is approximately 3.5-3.8% below annual-report reconstructed EV depending on whether leases are included in the EV bridge.

The most likely explanation is treatment difference rather than obvious provider error. Hero has a substantial current investment balance of INR 6,635.99 crore, cash and bank balances of INR 574.08 crore, current borrowings of INR 456.76 crore, lease liabilities of INR 243.17 crore, and minority interest of INR 132.05 crore. A provider that subtracts a broader investment set, excludes minority interest, excludes leases, or uses a different market-cap date can produce a materially different EV.

Hero is useful because it shows that even a mature, liquid, widely covered large-cap can fall into the moderate 2-5% deviation bucket when cash-like investments and consolidation adjustments are material.

## Data Quality Status

Status: annual-report note lock completed; provider date alignment and additional provider capture needed.

Completed items:

1. Uploaded and parsed Hero MotoCorp FY2024-25 annual report.
2. Completed annual-report note lock for current investments, cash, bank balances, current borrowings, lease liabilities, non-controlling interests, and non-current investments.
3. Captured preliminary StockAnalysis market cap and EV observations.
4. Built conservative and lease-and-minority-adjusted EV bridge views.

Open items:

1. Capture Yahoo Finance market cap and EV.
2. Capture Screener market cap and EV if visible.
3. Capture Moneycontrol current EV if visible.
4. Verify whether StockAnalysis EV includes leases and minority interest.
5. Convert this note into a formal output table.

## Current Pilot Signal

BEL currently looks like a low-deviation reliability benchmark.

NALCO currently looks like a moderate-deviation cash-rich commodity case.

Polycab currently looks like a low-deviation premium compounder under conservative treatment, but a moderate-definition-sensitivity case if acceptances are treated as debt-like obligations.

Hero MotoCorp currently looks like a moderate-deviation mature large-cap case driven by treatment of current investments, leases, minority interest, and market-cap timing.
