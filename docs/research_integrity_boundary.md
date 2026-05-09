# Research Integrity Boundary

## Purpose

This document defines the integrity rules for the enterprise value reconciliation project.

## Core Principle

The project does not assume that public financial-data providers are wrong. It tests whether provider-reported enterprise value is reconcilable with annual-report reconstructed enterprise value under a disclosed methodology.

## Facts, Assumptions, and Interpretation

Every research output should separate:

1. **Facts**: values directly observed in annual reports or provider pages.
2. **Assumptions**: treatment decisions, such as whether a current investment is cash-like.
3. **Interpretation**: conclusions about provider divergence, valuation multiple distortion, or reliability.

## No Invented Data

Missing values must be marked as missing. They must not be estimated silently.

If a provider does not display enterprise value, the record should use a missing-data flag rather than an inferred value unless the inference is clearly labelled and excluded from provider comparison.

## Source Documentation

Each annual-report extraction should include:

- annual report year,
- source URL or file name,
- page reference,
- note reference,
- line item name,
- extracted value,
- unit,
- treatment decision.

Each provider value should include:

- provider name,
- provider URL,
- access date,
- reported value,
- reported unit,
- data-quality flag.

## Language Discipline

Use neutral language:

- provider divergence,
- reconciliation difference,
- definition mismatch,
- timing mismatch,
- treatment difference.

Avoid strong claims such as:

- provider error,
- wrong EV,
- inaccurate database,
- distorted valuation,

unless the evidence clearly supports that wording.

## Pilot Discipline

The four-company pilot is a go/no-go test. If the pilot shows small deviations, the project should be reframed rather than forcing a dramatic conclusion.

## Investment Disclaimer

This project is not investment advice. It does not provide buy, sell, or hold recommendations. Enterprise value reconciliation is a data-quality and valuation-methodology exercise, not a security recommendation.

## Authorship and AI Use

AI tools may be used for code scaffolding, language refinement, consistency review, and document organization. Research design, data extraction, treatment decisions, interpretation, and final conclusions remain the responsibility of the authors.
