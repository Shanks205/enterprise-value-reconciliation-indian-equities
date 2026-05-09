# Enterprise Value Reconciliation in Indian Listed Equities

## A Multi-Provider Audit-Grade Comparison

This repository supports a research paper on enterprise value (EV) reconciliation for Indian listed equities. The project compares EV estimates from public financial-data providers against audit-grade EV reconstructed from annual-report disclosures for cash, bank balances, current investments, borrowings, lease liabilities, and other debt-like obligations.

## Working Paper Title

**Enterprise Value Reconciliation in Indian Equities: A Multi-Provider Audit-Grade Comparison Using Annual Report Data**

## Authors

- **Himanshu Dabi** — Independent Researcher, India
- **Hitesh Dabi** — Independent Researcher, India

## Research Objective

This project investigates whether publicly available financial-data providers report materially different enterprise value figures for Indian listed equities when compared with an annual-report-based reconstructed EV bridge.

The narrow research question is:

> How materially do enterprise value estimates from public financial-data providers differ from annual-report reconstructed enterprise value for Indian listed companies, and when do those differences distort valuation multiples such as EV/EBITDA and EV/Sales?

## Core Research Idea

Most investors and analysts use EV from platforms such as Yahoo Finance, Screener.in, Moneycontrol, and StockAnalysis without independently verifying the balance-sheet components behind the number. This project builds a reproducible framework to reconstruct EV from official company filings and compare that value against multiple public providers.

The paper does **not** assume that public providers are wrong. The objective is to test where provider EV estimates are reliable, where they diverge, and whether the divergence is economically meaningful.

## Pilot Companies

The initial go/no-go pilot covers four Indian listed companies:

| Company | Ticker | Reason for inclusion |
|---|---|---|
| Bharat Electronics Ltd | BEL.NS | Cash-rich defence electronics company; prior EV pilot exists |
| National Aluminium Company Ltd | NATIONALUM.NS | Cash-rich PSU commodity/metals company |
| Polycab India Ltd | POLYCAB.NS | Large quality compounder with premium valuation |
| Hero MotoCorp Ltd | HEROMOTOCO.NS | Large liquid mature cash-flow company |

The pilot will determine whether provider-level EV deviations are large enough to justify expanding the study to a larger 30–50 company sample.

## Provider Comparison

The pilot compares reconstructed EV against:

- Yahoo Finance
- Screener.in
- Moneycontrol
- StockAnalysis

Additional providers may be added only if their EV, market-cap, and balance-sheet definitions are sufficiently transparent.

## Reconstructed EV Formula

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

Where non-current investments are material, they are disclosed separately and included only when the treatment is economically justified.

## Go / No-Go Pilot Rule

| Pilot result | Decision |
|---|---|
| Average provider deviation below 2% | Reframe as reliability-and-exceptions paper |
| 2–5% deviation | Proceed cautiously with focus on edge cases |
| 5%+ deviation for at least one provider in at least two companies | Green light to expand sample |
| 10%+ deviation in cash-rich or debt-heavy cases | Strong empirical paper potential |

## Repository Structure

```text
enterprise-value-reconciliation-indian-equities/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/
│   │   ├── provider_snapshots/
│   │   ├── annual_report_extracts/
│   │   └── market_cap_snapshots/
│   ├── interim/
│   ├── processed/
│   └── templates/
│
├── docs/
│   ├── methodology_note.md
│   ├── data_dictionary.md
│   ├── sample_selection_protocol.md
│   ├── provider_definition_risks.md
│   └── research_integrity_boundary.md
│
├── scripts/
│   └── calculate_ev_deviation.py
│
├── src/
│   ├── ev_formula.py
│   ├── deviation_metrics.py
│   └── provider_cleaning.py
│
├── outputs/
│   ├── tables/
│   ├── charts/
│   └── research_tracker/
│
└── paper/
    ├── manuscript_v1.md
    └── appendices/
```

## Current Milestone

```text
Stage: Repository scaffold and four-company pilot setup
Current focus: Build data templates and methodology files
Next task: Collect provider EV values and annual-report EV bridge components for BEL, NALCO, Polycab, and Hero MotoCorp
```

## Research Integrity Rules

- Do not invent missing provider values.
- Record provider access date.
- Record annual-report source page or note reference.
- Separate provider EV, reconstructed EV, and interpretation.
- Mark missing or ambiguous values clearly.
- Treat small deviations honestly.
- Avoid language implying provider error unless the definition mismatch is documented.

## Disclaimer

This repository is for academic research and educational purposes only. It does not provide investment advice, valuation advice, financial advice, or buy/sell recommendations. All data should be independently verified before use in any investment or professional decision.
