# Sample Selection Protocol

## Purpose

This document defines how companies are selected for the enterprise value (EV) reconciliation study.

The sample-selection design must answer a likely reviewer question:

> Why were these companies selected, and why are they appropriate for a pilot study?

The answer is that the pilot is **not a performance test** and **not a stock recommendation exercise**. It is a methodological stress test of the EV reconciliation workflow across companies with different balance-sheet structures, business models, provider coverage, and valuation-use cases.

## Pilot Sample

The initial pilot contains four companies:

| Company | Ticker | Primary pilot role | Rationale |
|---|---|---|---|
| Bharat Electronics Ltd | BEL.NS | Cash-rich public-sector / defence electronics case | Prior EV reconciliation pilot exists; large cash and bank balances make EV bridge treatment important; strong public-provider coverage makes cross-provider comparison feasible. |
| National Aluminium Company Ltd | NATIONALUM.NS | Cash-rich commodity PSU case | Commodity cyclicality and substantial cash-like assets create a useful test of whether provider EV properly reflects net cash; PSU structure also tests public-sector balance-sheet treatment. |
| Polycab India Ltd | POLYCAB.NS | Quality compounder / premium valuation case | High-quality growth company where EV/EBITDA and EV/Sales are commonly used; useful to test whether EV differences affect valuation interpretation for premium-multiple companies. |
| Hero MotoCorp Ltd | HEROMOTOCO.NS | Large liquid mature cash-flow case | Large-cap, widely covered, mature operating business; acts as a control-style case where provider EV should be relatively reliable if data quality is strong. |

## Why Only These Four Companies in the Pilot?

The four-company pilot is intentionally small because the research question requires manual annual-report note locking. Before expanding to 30-50 companies, the project must first confirm whether cross-provider EV differences are economically meaningful enough to justify a larger empirical study.

A small pilot is appropriate because:

1. **Manual validation is expensive.** Each company requires extraction of cash, bank balances, investments, borrowings, lease liabilities, and related notes from the annual report.
2. **The project needs a go/no-go checkpoint.** If provider EV values are mostly within 1-2% of reconstructed EV, the full paper should be reframed as a reliability-and-exceptions study rather than a valuation-distortion study.
3. **The companies cover different balance-sheet archetypes.** The pilot includes cash-rich, PSU, commodity, mature large-cap, and premium compounder cases.
4. **All four companies are widely followed.** This improves the chance that provider data are available from Yahoo Finance, Screener.in, Moneycontrol, and StockAnalysis.
5. **The pilot tests methodology, not generalization.** The pilot is not used to make population-wide claims about Indian equities. It tests whether the methodology works and whether expansion is justified.

## Selection Criteria for the Pilot

The four pilot companies were selected using the following criteria:

| Criterion | Why it matters |
|---|---|
| Non-financial company | Enterprise value is more meaningful for operating companies than for banks, NBFCs, or insurers. |
| Publicly listed in India | Ensures availability of annual reports, market data, and provider snapshots. |
| Multiple provider coverage | The study requires EV or market-cap data from several public providers. |
| Annual-report data availability | Cash, investments, borrowings, and related notes must be extractable from FY2024-25 annual reports. |
| Balance-sheet diversity | The pilot must include companies where cash, investments, debt, or operating structure may affect EV calculation. |
| Valuation relevance | EV/EBITDA or EV/Sales should be meaningful for interpreting the company. |
| Prior research continuity | BEL and NALCO already appear in the earlier Monte Carlo DCF work, allowing continuity and methodology reuse. |

## Why These Four Are Good Pilot Candidates

### Bharat Electronics Ltd

BEL is a useful first pilot company because it is cash-rich, widely followed, and has a relatively clean borrowings profile. If provider EV and reconstructed EV are close for BEL, this creates a reliability benchmark. If they diverge, the divergence is important because BEL's cash balance is large enough to affect operating-business valuation multiples.

### NALCO

NALCO is useful because commodity companies require careful distinction between market capitalization, enterprise value, cash support, and mid-cycle operating value. Large cash-like assets can materially affect the EV bridge, especially when comparing commodity-cycle multiples.

### Polycab India

Polycab is useful because it is a high-quality compounder where investors often rely on EV/EBITDA and EV/Sales for valuation. Even a moderate EV difference can matter when a company trades at premium valuation multiples.

### Hero MotoCorp

Hero MotoCorp is useful because it is a mature, liquid, widely covered large-cap company. It functions as a control-style case. If public providers materially disagree even for a company like Hero MotoCorp, the case for broader EV reconciliation becomes stronger.

## Pilot Objective

The pilot is designed to test whether provider EV deviations are large enough to justify a larger paper.

The pilot is not designed to prove that providers are wrong. It is designed to test whether provider EV estimates differ from reconstructed EV in economically meaningful ways.

## Pilot Go / No-Go Rule

| Pilot result | Decision |
|---|---|
| Average provider deviation below 2% | Reframe as reliability-and-exceptions paper |
| 2-5% deviation | Proceed cautiously with focus on edge cases |
| 5%+ deviation for at least one provider in at least two companies | Green light to expand sample |
| 10%+ deviation in cash-rich or debt-heavy cases | Strong empirical paper potential |

## Expansion Sample

If the pilot receives a green light, the expanded sample should include 30-50 Indian listed companies across the following archetypes:

- cash-rich companies,
- debt-heavy companies,
- PSU companies,
- commodity and cyclical companies,
- quality compounders,
- capital goods and order-book companies,
- working-capital-sensitive companies,
- pharma and defensive companies,
- midcap industrial companies.

## Exclusions

The first version should generally exclude banks, NBFCs, insurers, and other financial institutions because enterprise value is less meaningful for financial firms and balance-sheet structure differs materially.

The project should also avoid companies with insufficient annual-report disclosure, unclear consolidated statements, or missing provider data unless they are used only as documented data-availability cases.

## Selection Principles for Expanded Sample

1. Include companies where EV is commonly used in valuation.
2. Include companies with different balance-sheet structures.
3. Include both large liquid companies and selected midcaps.
4. Avoid choosing companies only because they are expected to show large deviations.
5. Record the reason for inclusion.
6. Define categories before collecting provider EV values to reduce cherry-picking risk.
7. Preserve missing data rather than silently replacing it.

## Bias Control

The project should avoid cherry-picking. If the pilot expands, the expanded sample should use pre-defined categories and document inclusion logic before collecting provider EV values.

The paper should be honest even if the pilot finds low provider divergence. A low-divergence result still supports a reliability-and-exceptions paper, but it weakens any claim that provider EV values are systematically distorted.

## Recommended Expanded Sample Design

| Archetype | Target count |
|---|---:|
| Cash-rich / net-cash | 8-10 |
| Debt-heavy / capex-heavy | 8-10 |
| Commodity / cyclical | 6-8 |
| Quality compounder | 8-10 |
| Industrial / capital goods | 6-8 |
| Pharma / defensive | 4-6 |

The final sample size should remain manageable and reproducible.
