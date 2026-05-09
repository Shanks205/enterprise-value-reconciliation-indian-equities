# Enterprise Value Reconciliation in Indian Listed Equities

Audit-grade enterprise value reconciliation for Indian listed equities using annual reports and multi-provider EV comparisons.

## Research Objective

This project investigates whether publicly available financial-data providers report materially different Enterprise Value (EV) figures for Indian listed equities when compared with an annual-report-based reconstructed EV bridge.

The project focuses on a narrow but important question:

> Can Enterprise Value reported by public data providers be systematically reconciled against company annual reports, and where do material deviations arise?

## Core Research Idea

Most investors use EV from platforms such as Yahoo Finance, Screener.in, Moneycontrol, and StockAnalysis without independently verifying the balance-sheet components behind the number. This project builds a reproducible framework to reconstruct EV from official company filings and compare that value against multiple providers.

## Pilot Companies

The initial go/no-go pilot covers four Indian listed companies:

1. Bharat Electronics Ltd (BEL)
2. National Aluminium Company Ltd (NALCO)
3. Polycab India Ltd
4. Hero MotoCorp Ltd

The pilot will determine whether provider-level EV deviations are large enough to justify expanding the study to a larger 30-50 company sample.

## Provider Comparison

The pilot compares reconstructed EV against:

- Yahoo Finance
- Screener.in
- Moneycontrol
- StockAnalysis

## Reconstructed EV Formula

Enterprise Value is reconstructed as:

```text
Enterprise Value = Market Capitalization
                 + Total Debt
                 + Lease Liabilities
                 + Minority Interest
                 + Preference Capital
                 - Cash and Cash Equivalents
                 - Bank Balances / Cash-like Balances
                 - Current Investments / Liquid Investments
```

The exact classification depends on annual-report note disclosures and is documented in the methodology.

## Go / No-Go Rule

The full paper receives a green light if the four-company pilot shows:

- At least one provider has a 5%+ deviation from reconstructed EV, and
- This occurs for at least two of the four pilot companies.

If provider deviations are mostly below 1-2%, the paper will be reframed as a reliability-and-exceptions study rather than a valuation-distortion study.

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
│   ├── processed/
│   └── templates/
│
├── docs/
│   ├── methodology.md
│   └── pilot_plan.md
│
├── scripts/
│   └── calculate_ev_deviation.py
│
└── outputs/
    ├── tables/
    └── charts/
```

## Status

Current stage: **Pilot setup**

Next task: collect annual-report EV components and provider EV values for BEL, NALCO, Polycab, and Hero MotoCorp.

## Author

Himanshu Dabi

## Disclaimer

This project is for academic research and educational purposes only. It is not investment advice.
