# Methodology Note

## Purpose

This document defines the enterprise value reconciliation methodology used in the project.

The project compares provider-reported enterprise value against annual-report reconstructed enterprise value for Indian listed companies.

## Core Formula

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

## Why Enterprise Value Requires Reconciliation

Enterprise value is sensitive to provider definitions. Public financial-data platforms may differ in their treatment of:

- cash and cash equivalents,
- bank balances other than cash and cash equivalents,
- current investments,
- non-current investments,
- short-term borrowings,
- long-term borrowings,
- lease liabilities,
- acceptances,
- minority interest,
- preference capital,
- other debt-like obligations.

These differences can affect EV/EBITDA, EV/Sales, and operating-business multiple interpretation.

## Provider Data Layer

For each company, collect provider market capitalization and enterprise value from:

- Yahoo Finance
- Screener.in
- Moneycontrol
- StockAnalysis

Each provider snapshot must record:

- provider name,
- access date,
- company ticker or URL,
- reported market capitalization,
- reported enterprise value,
- currency and unit,
- notes on missing or ambiguous values.

## Annual-Report Reconstruction Layer

For each company, extract from the FY2024-25 annual report:

- cash and cash equivalents,
- bank balances other than cash and equivalents,
- current investments,
- non-current investments,
- short-term borrowings,
- long-term borrowings,
- current maturities of long-term debt,
- lease liabilities,
- preference capital,
- minority interest,
- any other debt-like obligation.

Each extraction must include:

- annual report year,
- source page number,
- source note number,
- extracted value,
- unit,
- treatment decision,
- reason for treatment.

## Treatment Rules

### Cash and cash equivalents

Subtract from EV reconstruction unless restricted or clearly not available to equity/debt holders.

### Bank balances other than cash and equivalents

Usually subtract if cash-like and liquid. If restricted, pledged, or legally constrained, disclose separately.

### Current investments

Subtract if liquid and cash-like. If operating, strategic, or illiquid, disclose separately and avoid automatic subtraction.

### Non-current investments

Do not automatically subtract. Include only if economically justified and clearly financial rather than operating/strategic.

### Borrowings

Add gross borrowings. Do not net borrowings against cash before reconstruction.

### Lease liabilities

Disclose separately. Include as debt-like obligations where material and comparable across companies.

## Deviation Metrics

```text
Absolute Deviation = Provider EV - Reconstructed EV
Percentage Deviation = Absolute Deviation / Reconstructed EV
Absolute Percentage Deviation = ABS(Percentage Deviation)
```

## Multiple Distortion Metrics

```text
Provider EV/EBITDA = Provider EV / EBITDA
Reconstructed EV/EBITDA = Reconstructed EV / EBITDA
EV/EBITDA Distortion = Provider EV/EBITDA - Reconstructed EV/EBITDA
```

Equivalent calculations may be used for EV/Sales.

## Pilot Decision Rule

| Pilot result | Decision |
|---|---|
| Average provider deviation below 2% | Reframe as reliability-and-exceptions paper |
| 2–5% deviation | Proceed cautiously with focus on edge cases |
| 5%+ deviation for at least one provider in at least two companies | Green light to expand sample |
| 10%+ deviation in cash-rich or debt-heavy cases | Strong empirical paper potential |

## Research Integrity Boundary

This project does not assume provider data are wrong. Provider-reported EV may differ from reconstructed EV because of valid definitional differences, timing differences, currency/unit differences, or data-update frequency.

The paper should use neutral language such as:

- provider divergence,
- definition mismatch,
- reconciliation difference,
- EV bridge treatment difference.

Avoid using the word “error” unless the provider value is clearly inconsistent with its own stated definition.
