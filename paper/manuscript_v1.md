# Enterprise Value Reconciliation in Indian Equities: A Multi-Provider Audit-Grade Comparison Using Annual Report Data

**Working Paper Draft v1**  
**Authors:** Himanshu Dabi and Hitesh Dabi  
**Status:** Early research draft  

## Abstract

This paper studies enterprise value reconciliation for Indian listed equities by comparing provider-reported enterprise value against enterprise value reconstructed from annual-report disclosures. Enterprise value is widely used in valuation multiples such as EV/EBITDA and EV/Sales, but public data providers may differ in their treatment of cash, bank balances, current investments, non-current investments, borrowings, lease liabilities, and other debt-like obligations. The study develops an audit-grade reconciliation workflow and applies it first to a four-company pilot sample: Bharat Electronics, NALCO, Polycab India, and Hero MotoCorp. The purpose is not to assume that provider data are wrong, but to test where provider EV estimates are reliable, where they diverge, and whether the divergence is economically meaningful enough to affect valuation interpretation.

## 1. Introduction

Enterprise value is one of the most frequently used bridge variables in equity valuation. Unlike market capitalization, enterprise value attempts to measure the value of the operating business available to all capital providers by adjusting equity value for debt, cash, and other balance-sheet items. In practice, analysts and investors often obtain enterprise value from public financial-data providers. These values are then used in valuation multiples, peer comparisons, investment screens, and research reports.

However, provider-reported enterprise value may not always be directly comparable across platforms. Differences can arise from market-cap timing, share-count updates, debt classification, lease treatment, cash and bank balance treatment, current investment treatment, and consolidated versus standalone data use. These differences are especially relevant for Indian listed companies with large cash balances, current investments, bank deposits, government ownership, commodity cycles, or complex financing structures.

This paper develops a reproducible annual-report-based enterprise value reconciliation framework for Indian listed equities. The initial objective is modest and empirical: to test whether provider EV values from public platforms materially differ from an audit-grade reconstructed EV bridge for selected Indian companies.

## 2. Research Question

The central research question is:

> How materially do enterprise value estimates from public financial-data providers differ from annual-report reconstructed enterprise value for Indian listed companies, and when do those differences distort valuation multiples such as EV/EBITDA and EV/Sales?

## 3. Contribution

This paper contributes in three ways.

First, it develops a narrow audit-grade EV bridge methodology for Indian listed equities using annual-report note disclosures.

Second, it compares reconstructed EV against multiple public providers rather than relying on a single source.

Third, it evaluates whether EV divergence is large enough to affect valuation multiple interpretation.

The paper is intentionally framed as a data-quality and valuation-methodology study, not as an investment recommendation paper.

## 4. Data and Sample

The first pilot sample includes four companies:

| Company | Ticker | Rationale |
|---|---|---|
| Bharat Electronics Ltd | BEL.NS | Cash-rich defence electronics company |
| National Aluminium Company Ltd | NATIONALUM.NS | Cash-rich PSU commodity/metals company |
| Polycab India Ltd | POLYCAB.NS | Quality compounder with premium valuation |
| Hero MotoCorp Ltd | HEROMOTOCO.NS | Mature large-cap cash-flow company |

Provider values will be collected from:

- Yahoo Finance
- Screener.in
- Moneycontrol
- StockAnalysis

Annual-report values will be extracted from FY2024-25 annual reports.

## 5. Methodology

The reconstructed enterprise value formula is:

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

Non-current investments are disclosed separately and included only when economically justified.

## 6. Deviation Metrics

For each provider-company pair:

```text
Absolute Deviation = Provider EV - Reconstructed EV
Percentage Deviation = Absolute Deviation / Reconstructed EV
Absolute Percentage Deviation = ABS(Percentage Deviation)
```

If EBITDA and revenue are available, multiple distortion is calculated as:

```text
EV/EBITDA Distortion = Provider EV/EBITDA - Reconstructed EV/EBITDA
EV/Sales Distortion = Provider EV/Sales - Reconstructed EV/Sales
```

## 7. Pilot Go / No-Go Rule

| Pilot result | Decision |
|---|---|
| Average provider deviation below 2% | Reframe as reliability-and-exceptions paper |
| 2–5% deviation | Proceed cautiously with focus on edge cases |
| 5%+ deviation for at least one provider in at least two companies | Green light to expand sample |
| 10%+ deviation in cash-rich or debt-heavy cases | Strong empirical paper potential |

## 8. Expected Results Format

The pilot will report:

1. Provider EV vs reconstructed EV by company.
2. Absolute and percentage deviation by provider.
3. Provider-level reliability summary.
4. Company-level case notes.
5. Whether deviations affect EV/EBITDA or EV/Sales materially.

## 9. Limitations

This study has several limitations. First, provider values may update at different times, creating timing mismatch. Second, annual-report reconstruction requires classification judgement, especially for current investments, bank balances, lease liabilities, and non-current investments. Third, the initial pilot sample is small and cannot support population-wide claims. Fourth, the study does not test whether EV differences predict stock returns or investment performance.

## 10. Research Integrity Boundary

The project does not assume that provider values are wrong. Differences may reflect valid definitional, timing, or classification choices. The paper uses neutral language such as provider divergence, reconciliation difference, and treatment mismatch unless an actual provider error is documented.

## 11. Conclusion

This draft establishes the research design for an enterprise value reconciliation study in Indian listed equities. The next step is to complete the four-company pilot and determine whether provider EV divergence is sufficiently material to justify expansion to a 30–50 company sample.

## References

References will be added after the pilot methodology and literature review are finalized.
