# Pilot Plan: Four-Company Enterprise Value Reconciliation

## 1. Objective

The pilot is designed to test whether multi-provider Enterprise Value (EV) deviations are large enough to justify a full SSRN-style research paper.

The pilot is not meant to prove the full thesis. It is a go/no-go signal test.

## 2. Pilot Companies

| Company | Ticker | Reason for Inclusion |
|---|---|---|
| Bharat Electronics Ltd | BEL | PSU, cash-rich balance sheet, useful test case for cash/current investment treatment |
| National Aluminium Company Ltd | NALCO | Commodity PSU with cash/investment classification relevance |
| Polycab India Ltd | POLYCAB | Private-sector industrial/consumer-electrical company with growth profile |
| Hero MotoCorp Ltd | HEROMOTOCO | Large private-sector manufacturing company with significant balance-sheet disclosures |

## 3. Providers to Compare

| Provider | Data to collect |
|---|---|
| Yahoo Finance | Enterprise Value |
| Screener.in | Enterprise Value / market cap and balance-sheet components where available |
| Moneycontrol | Enterprise Value / market cap / debt / cash where available |
| StockAnalysis | Enterprise Value |

## 4. Annual Report Reconstruction Steps

For each company:

1. Download the latest annual report.
2. Confirm whether the analysis uses consolidated or standalone financial statements.
3. Record market capitalization as of the provider data collection date.
4. Extract borrowings from notes.
5. Extract lease liabilities from notes.
6. Extract cash and cash equivalents from notes.
7. Extract bank balances other than cash and cash equivalents.
8. Extract current investments and classify whether they are liquid/cash-like.
9. Record minority interest if consolidated accounts are used.
10. Record preference capital if applicable.
11. Calculate reconstructed EV.
12. Compare provider EVs against reconstructed EV.

## 5. Required Source Locking

Every reconstructed EV component should include:

- Annual report year
- Page number
- Note number
- Exact line-item label
- Value
- Researcher decision: include / exclude / flag
- Comment explaining classification

## 6. Output Tables

### 6.1 Company EV Bridge

| Company | Component | Value INR crore | Source | Note/Page | Include in EV? | Comment |
|---|---:|---:|---|---|---|---|

### 6.2 Provider Comparison Table

| Company | Reconstructed EV | Yahoo EV | Screener EV | Moneycontrol EV | StockAnalysis EV | Max Absolute Deviation | Main Difference Driver |
|---|---:|---:|---:|---:|---:|---:|---|

### 6.3 Provider Deviation Table

| Company | Provider | Provider EV | Reconstructed EV | Deviation % | Absolute Deviation % | Materiality Bucket |
|---|---|---:|---:|---:|---:|---|

## 7. Materiality Buckets

| Absolute Deviation | Interpretation |
|---:|---|
| 0-2% | Immaterial |
| 2-5% | Moderate |
| 5-10% | Material |
| >10% | Highly material |

## 8. Go / No-Go Rule

Proceed to a full 30-50 company paper if:

- At least one provider has 5%+ absolute deviation, and
- This happens for at least two of the four pilot companies.

If deviations are below 1-2% for almost all providers and companies, reframe the project as:

> Provider Enterprise Value Reliability in Indian Equities: An Annual-Report Reconciliation Study

rather than:

> Enterprise Value Distortion in Indian Equity Databases

## 9. Immediate Next Task

Start with BEL because it is likely to reveal whether cash, bank balances, and current investments are being treated consistently across providers.

Recommended first file to complete:

```text
data/templates/ev_reconciliation_template.csv
```

Then duplicate the template manually for each company during data collection.
