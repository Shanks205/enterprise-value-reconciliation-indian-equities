# Appendix A: Pilot Data Collection Protocol

## Purpose

This appendix defines the protocol for collecting the four-company pilot data.

## Pilot Companies

1. Bharat Electronics Ltd (BEL.NS)
2. National Aluminium Company Ltd (NATIONALUM.NS)
3. Polycab India Ltd (POLYCAB.NS)
4. Hero MotoCorp Ltd (HEROMOTOCO.NS)

## Provider Snapshot Collection

For each company and provider, record:

- provider name,
- provider page URL,
- provider access date,
- reported market capitalization,
- reported enterprise value,
- reported unit,
- whether the value is consolidated or unclear,
- any provider definition notes.

Providers:

- Yahoo Finance
- Screener.in
- Moneycontrol
- StockAnalysis

## Annual Report Extraction

For each company, extract from FY2024-25 annual report:

- cash and cash equivalents,
- bank balances other than cash and equivalents,
- current investments,
- non-current investments, if material,
- short-term borrowings,
- long-term borrowings,
- current maturities of long-term debt,
- lease liabilities,
- minority interest,
- preference capital,
- other debt-like obligations.

Each extraction must include page and note references.

## Unit Standardization

All final processed values should be standardized to INR crore.

## Reconstructed EV Calculation

```text
Reconstructed EV = Market Capitalization
                 + Gross Borrowings
                 + Lease Liabilities and Other Debt-like Obligations
                 + Minority Interest, if material
                 + Preference Capital, if material
                 - Cash and Cash Equivalents
                 - Bank Balances Treated as Cash-like
                 - Current Investments Treated as Cash-like
```

## Deviation Calculation

```text
Absolute Deviation = Provider EV - Reconstructed EV
Percentage Deviation = Absolute Deviation / Reconstructed EV
Absolute Percentage Deviation = ABS(Percentage Deviation)
```

## Data Quality Flags

Use one of the following flags:

- verified
- needs_review
- missing_provider_data
- unit_unclear
- definition_mismatch
- manual_patch

## Pilot Interpretation

The pilot should be interpreted cautiously. A low deviation does not make the project useless; it suggests the paper should be framed around reliability and exceptions. A high deviation does not automatically prove provider error; it may reflect definition or timing mismatch.
