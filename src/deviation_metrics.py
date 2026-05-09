"""Deviation metrics for enterprise value reconciliation.

All monetary values should be standardized to INR crore before use.
"""

from __future__ import annotations

from typing import Optional


def safe_float(value: Optional[float]) -> float:
    """Convert None or blank-like values to 0.0."""
    if value is None:
        return 0.0
    return float(value)


def absolute_deviation(provider_ev: float, reconstructed_ev: float) -> float:
    """Provider EV minus reconstructed EV."""
    return safe_float(provider_ev) - safe_float(reconstructed_ev)


def percentage_deviation(provider_ev: float, reconstructed_ev: float) -> float:
    """Deviation as a percentage of reconstructed EV.

    Returns decimal form: 0.05 = 5%.
    """
    reconstructed_ev = safe_float(reconstructed_ev)
    if reconstructed_ev == 0:
        raise ValueError("reconstructed_ev cannot be zero")
    return absolute_deviation(provider_ev, reconstructed_ev) / reconstructed_ev


def absolute_percentage_deviation(provider_ev: float, reconstructed_ev: float) -> float:
    """Absolute percentage deviation in decimal form."""
    return abs(percentage_deviation(provider_ev, reconstructed_ev))


def deviation_bucket(abs_pct_deviation: float) -> str:
    """Classify deviation severity.

    Buckets are aligned with the pilot go/no-go rule.
    """
    value = abs(float(abs_pct_deviation))
    if value < 0.02:
        return "low_below_2pct"
    if value < 0.05:
        return "moderate_2_to_5pct"
    if value < 0.10:
        return "material_5_to_10pct"
    return "high_above_10pct"


def ev_multiple_distortion(provider_ev: float, reconstructed_ev: float, denominator: float) -> dict[str, float]:
    """Calculate EV multiple distortion.

    denominator can be EBITDA, sales, revenue, or another operating metric.
    """
    denominator = safe_float(denominator)
    if denominator == 0:
        raise ValueError("denominator cannot be zero")

    provider_multiple = safe_float(provider_ev) / denominator
    reconstructed_multiple = safe_float(reconstructed_ev) / denominator

    return {
        "provider_multiple": provider_multiple,
        "reconstructed_multiple": reconstructed_multiple,
        "multiple_distortion": provider_multiple - reconstructed_multiple,
    }
