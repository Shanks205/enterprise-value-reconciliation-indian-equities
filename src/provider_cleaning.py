"""Provider data cleaning helpers.

These functions standardize provider-reported market cap and enterprise value fields.
Final research outputs should keep raw provider values and cleaned values separately.
"""

from __future__ import annotations

import re
from typing import Optional


UNIT_MULTIPLIERS_TO_CRORE = {
    "crore": 1.0,
    "cr": 1.0,
    "million": 0.1,
    "mn": 0.1,
    "billion": 100.0,
    "bn": 100.0,
    "lakh": 0.01,
}


def normalize_unit(unit: str) -> str:
    """Normalize unit string to lowercase compact form."""
    return unit.strip().lower().replace(".", "")


def convert_to_inr_crore(value: float, unit: str) -> float:
    """Convert a numeric value into INR crore based on unit.

    This assumes the currency is already INR. Currency conversion is intentionally
    not handled here because provider currency should be explicitly verified.
    """
    normalized_unit = normalize_unit(unit)
    if normalized_unit not in UNIT_MULTIPLIERS_TO_CRORE:
        raise ValueError(f"Unsupported unit: {unit}")
    return float(value) * UNIT_MULTIPLIERS_TO_CRORE[normalized_unit]


def parse_number(text: Optional[str]) -> Optional[float]:
    """Parse a loose numeric string into a float.

    Examples:
        "327,185" -> 327185.0
        "₹ 3,271.85 Cr" -> 3271.85
    """
    if text is None:
        return None
    cleaned = text.replace(",", "")
    match = re.search(r"-?\d+(?:\.\d+)?", cleaned)
    if not match:
        return None
    return float(match.group(0))


def standardize_provider_name(name: str) -> str:
    """Standardize provider names."""
    mapping = {
        "yahoo": "Yahoo Finance",
        "yahoo finance": "Yahoo Finance",
        "screener": "Screener.in",
        "screener.in": "Screener.in",
        "moneycontrol": "Moneycontrol",
        "stockanalysis": "StockAnalysis",
        "stockanalysis.com": "StockAnalysis",
    }
    key = name.strip().lower()
    return mapping.get(key, name.strip())
