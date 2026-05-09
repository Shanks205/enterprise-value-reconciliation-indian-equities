# Project Roadmap

## Project

**Enterprise Value Reconciliation in Indian Equities: A Multi-Provider Audit-Grade Comparison Using Annual Report Data**

## Authors

- Himanshu Dabi
- Hitesh Dabi

## Current Stage

Stage 1: Four-company pilot setup.

The immediate objective is to test whether public provider EV values diverge meaningfully from annual-report reconstructed EV for a small pilot sample before expanding to a 30-50 company study.

## Pilot Sample

| Company | Ticker | Role in pilot |
|---|---|---|
| Bharat Electronics Ltd | BEL.NS | Cash-rich defence electronics / prior EV pilot |
| National Aluminium Company Ltd | NATIONALUM.NS | Cash-rich PSU commodity/metals company |
| Polycab India Ltd | POLYCAB.NS | Quality compounder / premium valuation case |
| Hero MotoCorp Ltd | HEROMOTOCO.NS | Mature large-cap cash-flow company |

## Milestones

### Milestone 1 — Repository scaffold

Status: complete.

Deliverables:

- README research design
- methodology note
- data dictionary
- sample selection protocol
- provider definition risks note
- research integrity boundary
- initial manuscript draft
- EV formula module
- deviation metrics module
- provider cleaning module
- data templates

### Milestone 2 — Four-company pilot data collection

Status: in progress.

Tasks:

1. Collect provider market cap and EV values for each pilot company.
2. Record provider access dates and URLs.
3. Extract annual-report cash, bank balance, investment, borrowings, and lease liability fields.
4. Record source page and note references.
5. Standardize all values to INR crore.
6. Compute reconstructed EV.
7. Compare provider EV against reconstructed EV.
8. Classify deviation materiality.

### Milestone 3 — Pilot go/no-go decision

Status: pending.

Decision rule:

| Pilot result | Decision |
|---|---|
| Average provider deviation below 2% | Reframe as reliability-and-exceptions paper |
| 2-5% deviation | Proceed cautiously with focus on edge cases |
| 5%+ deviation for at least one provider in at least two companies | Green light to expand sample |
| 10%+ deviation in cash-rich or debt-heavy cases | Strong empirical paper potential |

### Milestone 4 — Expanded sample

Status: pending.

Target sample size: 30-50 companies.

Target archetypes:

- cash-rich / net-cash companies
- debt-heavy / capex-heavy companies
- PSU companies
- commodity / cyclical companies
- quality compounders
- capital goods / order-book companies
- working-capital-sensitive companies
- pharma and defensive companies

### Milestone 5 — SSRN draft

Status: pending.

Deliverables:

- full manuscript draft
- abstract
- methodology
- results tables
- case studies
- limitations
- references
- reproducibility appendix

## Immediate Next Task

Complete the BEL pilot row first because prior work already contains BEL cash and bank-balance note-lock information. After BEL, complete NALCO, then Polycab and Hero MotoCorp.
