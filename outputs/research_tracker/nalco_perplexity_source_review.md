# NALCO Perplexity Source Review

## Source

Perplexity Finance / Perplexity search output supplied by the author.

## Company

National Aluminium Company Ltd (NATIONALUM.NS)

## Purpose

This note records the Perplexity-supplied provider snapshot as a source-discovery layer. The Perplexity output is useful for identifying provider pages and approximate EV / market capitalization values, but it should not be treated as the final primary source.

Primary verification should still come from:

- provider pages directly,
- annual reports,
- company filings,
- manually captured snapshots.

## Provider Values Reported by Perplexity Output

| Provider | Page date / context | Market cap (INR crore) | Enterprise value (INR crore) | Status |
|---|---:|---:|---:|---|
| Yahoo Finance | Around May 2026 | 74,209 | 66,274 | Useful provider snapshot; needs direct source verification |
| Moneycontrol | 08 May 2026 | 73,823 | Not visible | Market cap useful; EV not visible |
| Screener.in | Recent / unclear | Not visible | Not visible | Output appears to point to a generic EV screen and possible wrong entity issue; needs manual verification |
| StockAnalysis | Around Aug 2025 / unclear | 73,337 | 64,696 | Useful but date alignment unclear |

## Annual-Report Extraction Status in Perplexity Output

The Perplexity output did not extract the FY2024-25 annual-report EV bridge items. It marked the following fields as not available:

- cash and cash equivalents,
- bank balances other than cash,
- current investments,
- non-current investments,
- short-term borrowings,
- long-term borrowings,
- current maturities of long-term debt,
- lease liabilities,
- minority interest,
- preference capital,
- other debt-like obligations.

The output did identify the FY2024-25 annual-report URL:

```text
https://nalcoindia.com/wp-content/uploads/2025/09/44th-Annual-Report-2024-25-NALCO.pdf
```

## Important Review Notes

1. Perplexity is useful for source discovery but not enough for final audit-grade extraction.
2. Provider dates are not fully aligned.
3. Screener result may not directly represent the correct NALCO company page and requires manual verification.
4. Moneycontrol EV remains not visible in the Perplexity output.
5. The annual-report note-lock extraction still needs to be completed from the actual FY2024-25 annual report.

## Updated NALCO Research Interpretation

The Perplexity output strengthens the preliminary finding that NALCO may be a moderate provider-divergence case. Yahoo Finance and StockAnalysis both show provider EV below their respective market capitalization by roughly INR 7,900 crore to INR 8,600 crore, which is directionally consistent with a cash-rich balance sheet.

However, final conclusions should wait until:

- provider dates are aligned,
- FY2024-25 annual-report cash/debt/investment notes are directly extracted,
- Moneycontrol and Screener EV visibility is manually checked,
- units are standardized to INR crore.

## Data-Quality Classification

Current status: preliminary, needs review.

Use in final paper: source-discovery support only unless direct source verification is completed.
