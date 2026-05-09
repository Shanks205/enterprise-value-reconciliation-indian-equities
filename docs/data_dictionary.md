# Data Dictionary

This document defines the main fields used in the enterprise value reconciliation project.

## Company Identification

| Field | Description |
|---|---|
| company | Company name |
| ticker | NSE/BSE ticker or provider ticker |
| sector | Business sector |
| archetype | Balance-sheet or valuation archetype, such as cash-rich, debt-heavy, commodity, PSU, quality compounder |
| valuation_date | Fixed date for provider comparison |

## Provider Snapshot Fields

| Field | Description |
|---|---|
| provider | Data provider name |
| provider_url | URL of the provider page |
| provider_access_date | Date the provider page was accessed |
| provider_market_cap | Market capitalization reported by provider |
| provider_ev | Enterprise value reported by provider |
| provider_currency | Currency used by provider |
| provider_unit | Unit used by provider, such as crore, million, billion |
| provider_notes | Notes on provider definitions, missing values, or data issues |

## Annual Report Extraction Fields

| Field | Description |
|---|---|
| annual_report_year | Financial year of annual report used |
| annual_report_url | Source URL for annual report |
| page_reference | Page number in annual report |
| note_reference | Financial statement note number |
| cash_and_equivalents | Cash and cash equivalents |
| bank_balances | Bank balances other than cash and equivalents |
| current_investments | Current investments |
| non_current_investments | Non-current investments |
| short_term_borrowings | Short-term borrowings |
| long_term_borrowings | Long-term borrowings |
| current_maturities | Current maturities of long-term debt |
| lease_liabilities | Lease liabilities |
| minority_interest | Minority interest, if material |
| preference_capital | Preference capital, if material |
| other_debt_like_items | Other debt-like obligations |
| extraction_notes | Notes on classification and treatment decisions |

## Reconciliation Fields

| Field | Description |
|---|---|
| reconstructed_ev | Annual-report reconstructed enterprise value |
| absolute_deviation | Provider EV minus reconstructed EV |
| percentage_deviation | Absolute deviation divided by reconstructed EV |
| absolute_percentage_deviation | Absolute value of percentage deviation |
| deviation_bucket | Classification such as low, moderate, high, severe |
| ev_ebitda_provider | Provider EV divided by EBITDA |
| ev_ebitda_reconstructed | Reconstructed EV divided by EBITDA |
| ev_ebitda_distortion | Difference between provider and reconstructed EV/EBITDA |
| ev_sales_provider | Provider EV divided by revenue/sales |
| ev_sales_reconstructed | Reconstructed EV divided by revenue/sales |
| ev_sales_distortion | Difference between provider and reconstructed EV/Sales |

## Data Quality Flags

| Flag | Meaning |
|---|---|
| verified | Source and treatment are clear |
| needs_review | Value extracted but treatment uncertain |
| missing_provider_data | Provider value not available |
| unit_unclear | Provider or annual-report unit requires confirmation |
| definition_mismatch | Provider definition may not match reconstructed formula |
| manual_patch | Value required manual correction or standardization |

## Units

All final processed values should be standardized to Indian rupees crore unless otherwise stated.
