"""Calculate Enterprise Value provider deviations.

This script reads the pilot EV reconciliation CSV and calculates:
- reconstructed enterprise value, if component fields are available
- provider deviation percentage
- absolute deviation percentage
- materiality bucket

Usage:
    python scripts/calculate_ev_deviation.py

Expected input:
    data/templates/ev_reconciliation_template.csv

Recommended workflow:
    1. Copy the template into data/processed/pilot_ev_reconciliation.csv
    2. Fill in reconstructed EV components and provider EV values
    3. Run this script
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "data" / "processed" / "pilot_ev_reconciliation.csv"
TEMPLATE_INPUT = ROOT / "data" / "templates" / "ev_reconciliation_template.csv"
DEFAULT_OUTPUT = ROOT / "outputs" / "tables" / "provider_ev_deviation_results.csv"


ADD_COMPONENTS = [
    "market_cap_inr_crore",
    "total_borrowings_inr_crore",
    "lease_liabilities_inr_crore",
    "minority_interest_inr_crore",
    "preference_capital_inr_crore",
]

SUBTRACT_COMPONENTS = [
    "cash_and_equivalents_inr_crore",
    "bank_balances_inr_crore",
    "current_investments_inr_crore",
    "other_cash_like_assets_inr_crore",
]


def materiality_bucket(abs_deviation: float) -> str:
    """Classify EV deviation into research materiality buckets."""
    if pd.isna(abs_deviation):
        return "missing"
    if abs_deviation <= 2:
        return "immaterial_0_2pct"
    if abs_deviation <= 5:
        return "moderate_2_5pct"
    if abs_deviation <= 10:
        return "material_5_10pct"
    return "highly_material_above_10pct"


def calculate_reconstructed_ev(df: pd.DataFrame) -> pd.Series:
    """Calculate reconstructed EV from component columns where available."""
    for col in ADD_COMPONENTS + SUBTRACT_COMPONENTS:
        if col not in df.columns:
            df[col] = np.nan
        df[col] = pd.to_numeric(df[col], errors="coerce")

    add_total = df[ADD_COMPONENTS].sum(axis=1, min_count=1)
    subtract_total = df[SUBTRACT_COMPONENTS].sum(axis=1, min_count=1)
    calculated_ev = add_total - subtract_total

    existing_ev = pd.to_numeric(df.get("reconstructed_ev_inr_crore"), errors="coerce")
    return existing_ev.fillna(calculated_ev)


def main() -> None:
    input_path = DEFAULT_INPUT if DEFAULT_INPUT.exists() else TEMPLATE_INPUT

    if not input_path.exists():
        raise FileNotFoundError(
            "No input file found. Create data/processed/pilot_ev_reconciliation.csv "
            "or keep the template at data/templates/ev_reconciliation_template.csv."
        )

    df = pd.read_csv(input_path)
    df["reconstructed_ev_inr_crore"] = calculate_reconstructed_ev(df)
    df["provider_ev_inr_crore"] = pd.to_numeric(df.get("provider_ev_inr_crore"), errors="coerce")

    df["deviation_pct"] = (
        (df["provider_ev_inr_crore"] - df["reconstructed_ev_inr_crore"])
        / df["reconstructed_ev_inr_crore"]
        * 100
    )
    df["absolute_deviation_pct"] = df["deviation_pct"].abs()
    df["materiality_bucket"] = df["absolute_deviation_pct"].apply(materiality_bucket)

    DEFAULT_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(DEFAULT_OUTPUT, index=False)

    print(f"Input file: {input_path.relative_to(ROOT)}")
    print(f"Output file: {DEFAULT_OUTPUT.relative_to(ROOT)}")

    summary_cols = [
        "company",
        "provider_name",
        "reconstructed_ev_inr_crore",
        "provider_ev_inr_crore",
        "deviation_pct",
        "absolute_deviation_pct",
        "materiality_bucket",
    ]
    available_cols = [col for col in summary_cols if col in df.columns]
    print(df[available_cols].to_string(index=False))


if __name__ == "__main__":
    main()
