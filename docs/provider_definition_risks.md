# Provider Definition Risks

## Purpose

This note documents why enterprise value can differ across public data providers even when none of the providers are necessarily wrong.

## Main Sources of Provider EV Divergence

### 1. Market Capitalization Timing

Market capitalization changes daily. If provider EV values use different market-cap dates or delayed share-count updates, EV may differ even when cash and debt treatment is similar.

### 2. Cash and Bank Balance Treatment

Some providers may subtract only cash and cash equivalents. Others may also subtract bank balances, short-term deposits, or cash-like financial assets.

### 3. Current Investment Treatment

Current investments may be liquid and cash-like, but provider treatment is not always visible. Some platforms may subtract them; others may not.

### 4. Non-Current Investment Treatment

Non-current investments can be strategic, operating, financial, liquid, or illiquid. Automatic subtraction can create comparability problems.

### 5. Lease Liability Treatment

Lease liabilities may or may not be included as debt-like obligations. Differences are especially relevant after Ind AS lease accounting changes.

### 6. Borrowings Classification

Short-term borrowings, current maturities of long-term debt, cash credit, acceptances, and other facilities may be classified differently across statements and providers.

### 7. Consolidated vs Standalone Data

Some providers may use consolidated values while others expose standalone or mixed fields. This is a major source of hidden inconsistency.

### 8. Currency and Unit Differences

Provider values may be shown in crore, million, billion, or abbreviated market units. Unit errors can create false deviations.

### 9. Update Frequency

Provider EV may combine a current market capitalization with stale balance-sheet data. This can create timing mismatch.

### 10. Missing Definition Disclosure

Many platforms show EV without fully disclosing the exact calculation. This project treats such values as provider-reported EV, not as audit-grade values.

## Research Language Rule

Use neutral terms unless an actual error is proven:

- provider divergence
- reconciliation difference
- definition mismatch
- timing mismatch
- treatment difference

Avoid saying “provider error” unless the value is clearly inconsistent with the provider's own definition or with obvious arithmetic.
