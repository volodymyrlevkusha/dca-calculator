# src/dca_calculator/core.py
from __future__ import annotations

def monthly_rate_from_apy(apy_percent: float) -> float:
    """
    Convert annual percentage yield (APY, in %) to an equivalent monthly compound rate.
    Example: 10 -> ~0.007974 (0.7974% per month)
    """
    apy = apy_percent / 100.0
    return (1.0 + apy) ** (1.0 / 12.0) - 1.0


def dca_calculate(
    monthly_contribution: float,
    apy_percent: float,
    months: int,
    timing: str = "end",
) -> dict:
    """
    Calculate DCA future value with compound interest.

    Args:
        monthly_contribution: How much you invest each month (>= 0).
        apy_percent: Annual percentage yield, e.g. 8.2 for 8.2%.
        months: Number of months (>= 1).
        timing:
            - "end"  : contribution happens at the end of each month (ordinary annuity)
            - "begin": contribution happens at the beginning of each month (annuity due)

    Returns:
        dict with:
            total, principal, extra, roi, monthly_rate
    """
    if months < 1:
        raise ValueError("months must be >= 1")
    if monthly_contribution < 0:
        raise ValueError("monthly_contribution must be >= 0")

    monthly_rate = monthly_rate_from_apy(apy_percent)
    total = 0.0

    if timing == "end":
        for _ in range(months):
            total = total * (1.0 + monthly_rate) + monthly_contribution
    elif timing == "begin":
        for _ in range(months):
            total = (total + monthly_contribution) * (1.0 + monthly_rate)
    else:
        raise ValueError("timing must be 'end' or 'begin'")

    principal = monthly_contribution * months
    extra = total - principal
    roi = (extra / principal) * 100.0 if principal > 0 else 0.0

    return {
        "total": total,
        "principal": principal,
        "extra": extra,
        "roi": roi,
        "monthly_rate": monthly_rate,
    }
