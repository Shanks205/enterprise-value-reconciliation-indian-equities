# Methodology: Annual-Report-Based Enterprise Value Reconstruction

## 1. Purpose

This methodology defines how Enterprise Value (EV) will be reconstructed from company annual reports and compared against publicly available provider-reported EV figures.

The project is designed as a reproducible reconciliation framework rather than a simple valuation screen.

## 2. Research Question

Do public financial-data providers report Enterprise Value figures for Indian listed equities that materially differ from an annual-report-based reconstructed EV bridge?

## 3. Unit of Analysis

The unit of analysis is a listed Indian company-year observation.

For the pilot stage, the sample includes four companies:

- Bharat Electronics Ltd (BEL)
- National Aluminium Company Ltd (NALCO)
- Polycab India Ltd
- Hero MotoCorp Ltd

## 4. Reconstructed Enterprise Value Formula

The base formula is:

```text
EV = Market Capitalization
   + Total Borrowings
   + Lease Liabilities
   + Minority Interest
   + Preference Capital
   - Cash and Cash Equivalents
   - Bank Balances / Cash-like Balances
   - Current Investments / Liquid Investments
```

## 5. Component Definitions

### 5.1 Market Capitalization

Market capitalization is calculated as:

```text
Market Capitalization = Share Price × Shares Outstanding
```

The market price date must be recorded. If provider EV values are collected on a specific date, the reconstructed market capitalization should use the same or nearest available date.

### 5.2 Total Borrowings

Total borrowings include:

- Non-current borrowings
- Current borrowings
- Short-term debt
- Long-term debt due within one year
- Other interest-bearing financial liabilities where disclosed

Borrowings should be sourced from annual-report balance-sheet notes, not only from the face of the balance sheet.

### 5.3 Lease Liabilities

Lease liabilities should be included when they are financing-like obligations. These may appear as:

- Current lease liabilities
- Non-current lease liabilities
- Finance lease obligations

The treatment should be disclosed consistently.

### 5.4 Cash and Cash Equivalents

Cash and cash equivalents should be taken from the company annual report and note disclosures. Items may include:

- Cash on hand
- Balances with banks
- Cheques/drafts on hand
- Deposits with original maturity of three months or less

### 5.5 Bank Balances Other Than Cash and Cash Equivalents

Indian annual reports often separate bank balances from cash and cash equivalents. These may include:

- Earmarked balances
- Unpaid dividend accounts
- Margin money deposits
- Deposits with maturity greater than three months but less than twelve months

Only liquid, cash-like balances should be subtracted from EV. Restricted balances should be flagged and justified.

### 5.6 Current Investments / Liquid Investments

Current investments may be cash-like if they are highly liquid and held in instruments such as:

- Mutual funds
- Treasury bills
- Short-term deposits
- Liquid funds

Each inclusion must be supported by the annual-report note.

### 5.7 Minority Interest

Minority interest should be added when using consolidated financial statements. It should be taken from the equity section of the consolidated balance sheet.

### 5.8 Preference Capital

Preference capital should be added if it behaves like a financing claim. The classification should be documented from the relevant equity/liability note.

## 6. Note-Locking Protocol

Each EV component must be note-locked.

A note-locked value records:

- Company name
- Financial year
- EV component
- Reported value
- Annual report page number
- Annual report note number
- Exact label used by the company
- Inclusion/exclusion decision
- Researcher comment

This is the main methodological contribution of the project.

## 7. Provider EV Collection

For each company, provider EV values will be collected from:

- Yahoo Finance
- Screener.in
- Moneycontrol
- StockAnalysis

For every provider observation, record:

- Provider name
- Collection date
- EV value
- Currency/unit
- URL
- Notes on visible methodology, if available

## 8. Deviation Calculation

Deviation is calculated as:

```text
Provider EV Deviation (%) = (Provider EV - Reconstructed EV) / Reconstructed EV × 100
```

Absolute deviation is calculated as:

```text
Absolute Deviation (%) = |Provider EV Deviation (%)|
```

## 9. Materiality Thresholds

The pilot uses the following interpretation:

| Absolute deviation | Interpretation |
|---:|---|
| 0-2% | Immaterial / provider broadly aligned |
| 2-5% | Moderate difference requiring explanation |
| 5-10% | Material difference |
| >10% | Highly material difference |

## 10. Pilot Go / No-Go Rule

The full paper receives a green light if:

- At least one provider shows 5%+ deviation, and
- This occurs in at least two of the four pilot companies.

If deviations are mostly below 1-2%, the paper will be reframed around provider reliability, methodological transparency, and exceptional cases.

## 11. Limitations

Potential limitations include:

- Differences in market price dates
- Differences in consolidated vs standalone reporting
- Provider methodology opacity
- Provider update timing
- Restricted cash classification uncertainty
- Treatment of leases and current investments

## 12. Research Output

The final project should produce:

- A GitHub repository with reproducible templates and scripts
- A pilot evidence table
- Company-level EV bridge sheets
- Provider deviation charts
- A draft SSRN paper
