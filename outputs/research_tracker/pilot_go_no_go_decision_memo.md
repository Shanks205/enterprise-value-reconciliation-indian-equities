# Pilot Go / No-Go Decision Memo

## Project

**Enterprise Value Reconciliation in Indian Equities: A Multi-Provider Audit-Grade Comparison Using Annual Report Data**

## Authors

- Himanshu Dabi
- Hitesh Dabi

## Purpose

This memo converts the four-company pilot into a preliminary go/no-go research decision. It is not a final paper conclusion. It is an internal research checkpoint used to decide whether the project should proceed to an expanded 30-50 company sample.

## Pilot Companies Reviewed

| Company | Ticker | Pilot role |
|---|---|---|
| Bharat Electronics Ltd | BEL.NS | Cash-rich defence electronics reliability benchmark |
| National Aluminium Company Ltd | NATIONALUM.NS | Cash-rich PSU commodity/metals case |
| Polycab India Ltd | POLYCAB.NS | Premium compounder with working-capital financing sensitivity |
| Hero MotoCorp Ltd | HEROMOTOCO.NS | Mature large-cap cash-flow company with current-investment and consolidation sensitivity |

## Current Pilot Evidence

| Company | Current signal | Approximate deviation range | Materiality bucket | Main EV issue |
|---|---|---:|---|---|
| BEL | Low-deviation reliability benchmark | about 0.5% | Low | Cash and bank-balance treatment; provider EV appears close to reconstructed EV |
| NALCO | Moderate-deviation cash-rich commodity case | about 2.8% to 4.1% | Moderate | Cash, current investments, provider timing, possible lease treatment |
| Polycab | Low under conservative bridge; moderate under full debt-like sensitivity | about 1.1% conservative; about 2.2% full sensitivity | Low to moderate | Acceptances and working-capital financing treatment |
| Hero MotoCorp | Moderate-deviation mature large-cap case | about 3.5% to 3.8% | Moderate | Current investments, leases, non-controlling interest, market-cap timing |

## Go / No-Go Rule Applied

| Pilot result | Decision rule |
|---|---|
| Average provider deviation below 2% | Reframe as reliability-and-exceptions paper |
| 2-5% deviation | Proceed cautiously with focus on edge cases |
| 5%+ deviation for at least one provider in at least two companies | Green light to expand sample |
| 10%+ deviation in cash-rich or debt-heavy cases | Strong empirical paper potential |

## Current Decision

```text
Proceed, but with cautious framing.
```

The pilot does not yet justify an aggressive claim that public financial-data providers systematically misstate enterprise value. However, it does justify continuing the project because the pilot shows economically meaningful moderate divergence in NALCO and Hero MotoCorp, and a definitional sensitivity case in Polycab.

## Recommended Framing

The strongest framing is:

> Provider enterprise value is often directionally reasonable for large Indian listed companies, but moderate and economically meaningful divergence can arise when current investments, cash-like bank balances, lease liabilities, minority interest, acceptances, or timing differences are material.

Avoid framing the paper as:

> Public providers are wrong.

Use instead:

> Provider EV values require reconciliation before being used in valuation multiples, especially for cash-rich, investment-heavy, lease-sensitive, or working-capital-financed companies.

## Expansion Decision

The pilot supports expansion to a larger sample, but the first expansion should be controlled.

Recommended next sample size:

```text
30 companies first, not 50 immediately.
```

Rationale:

1. Annual-report note locking is manual and time-consuming.
2. Provider values require date-alignment checks.
3. A 30-company sample is large enough to test patterns without overwhelming the research workflow.
4. If the 30-company result remains useful, the paper can later expand to 50 companies.

## Recommended Expanded Sample Structure

| Archetype | Target count | Purpose |
|---|---:|---|
| Cash-rich / net-cash companies | 5 | Test cash and current-investment treatment |
| Debt-heavy / capex-heavy companies | 5 | Test borrowings and lease treatment |
| Commodity / cyclical companies | 5 | Test volatile balance-sheet and cycle-sensitive EV interpretation |
| Quality compounders | 5 | Test premium multiple sensitivity |
| Industrial / capital goods companies | 5 | Test working capital and order-book businesses |
| Pharma / defensive companies | 5 | Test cash-heavy but stable operating businesses |

Total initial expansion sample: 30 companies.

## Immediate Next Step

Before selecting the full 30-company list, complete a provider-date-alignment protocol.

This protocol should define:

1. What date is used for market capitalization.
2. Whether provider EV and market cap are captured on the same date.
3. How to treat provider values that show ratio-table EV from older fiscal periods.
4. How to mark missing provider EV.
5. Whether the base EV bridge includes leases.
6. How minority interest is handled for consolidated companies.
7. How acceptances and working-capital financing are handled.

## Next File To Create

```text
docs/provider_date_alignment_protocol.md
```

This should be created before expanding the sample.
