"""Enterprise value reconstruction formulas.

All final values should be standardized to INR crore before calling these functions.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class EVInputs:
    """Inputs required to reconstruct enterprise value."""

    market_cap: float
    gross_borrowings: float = 0.0
    lease_liabilities: float = 0.0
    other_debt_like_items: float = 0.0
    minority_interest: float = 0.0
    preference_capital: float = 0.0
    cash_and_equivalents: float = 0.0
    bank_balances_cash_like: float = 0.0
    current_investments_cash_like: float = 0.0
    non_current_investments_cash_like: float = 0.0
    include_non_current_investments: bool = False


def _safe(value: Optional[float]) -> float:
    """Convert None to zero while preserving numeric values."""
    return 0.0 if value is None else float(value)


def reconstruct_ev(inputs: EVInputs) -> float:
    """Reconstruct enterprise value from annual-report components.

    Formula:
        EV = Market Cap
             + gross borrowings
             + lease liabilities
             + other debt-like obligations
             + minority interest
             + preference capital
             - cash and equivalents
             - cash-like bank balances
             - cash-like current investments
             - cash-like non-current investments, only if explicitly included
    """

    debt_like = (
        _safe(inputs.gross_borrowings)
        + _safe(inputs.lease_liabilities)
        + _safe(inputs.other_debt_like_items)
        + _safe(inputs.minority_interest)
        + _safe(inputs.preference_capital)
    )

    cash_like = (
        _safe(inputs.cash_and_equivalents)
        + _safe(inputs.bank_balances_cash_like)
        + _safe(inputs.current_investments_cash_like)
    )

    if inputs.include_non_current_investments:
        cash_like += _safe(inputs.non_current_investments_cash_like)

    return _safe(inputs.market_cap) + debt_like - cash_like


def calculate_deviation(provider_ev: float, reconstructed_ev: float) -> dict[str, float]:
    """Calculate provider EV deviation from reconstructed EV."""
    provider_ev = _safe(provider_ev)
    reconstructed_ev = _safe(reconstructed_ev)

    if reconstructed_ev == 0:
        raise ValueError("reconstructed_ev cannot be zero")

    absolute_deviation = provider_ev - reconstructed_ev
    percentage_deviation = absolute_deviation / reconstructed_ev

    return {
        "absolute_deviation": absolute_deviation,
        "percentage_deviation": percentage_deviation,
        "absolute_percentage_deviation": abs(percentage_deviation),
    }


if __name__ == "__main__":
    # Example only. Replace with company-specific inputs from templates.
    example = EVInputs(
        market_cap=327_185.0,
        gross_borrowings=0.0,
        cash_and_equivalents=713.45,
        bank_balances_cash_like=8_831.65,
    )
    print(round(reconstruct_ev(example), 2))
