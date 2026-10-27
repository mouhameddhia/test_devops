"""Refund calculation for the payment service.

This module provides a utility function to compute the refundable amount
after applying a service fee expressed as a percentage of the original
transaction amount.
"""

from __future__ import annotations


def calculate_refund(amount: int | float, fee_percent: int | float = 15) -> float:
    """Return the refund amount after deducting the service fee.

    Args:
        amount: The original transaction amount. Must be a numeric type.
        fee_percent: The service fee expressed as a percentage of ``amount``.
            Must be a numeric type. Defaults to ``15`` (i.e., 15 %).

    Returns:
        The amount remaining after the fee has been deducted, as a ``float``.

    The fee is calculated as ``amount * fee_percent / 100``. For example,
    ``calculate_refund(100)`` returns ``85.0`` because a 15 % fee on 100 is
    15, leaving 85.
    """
    # Validate input types
    if not isinstance(amount, (int, float)):
        raise TypeError("amount must be a number")
    if not isinstance(fee_percent, (int, float)):
        raise TypeError("fee_percent must be a number")

    fee = amount * fee_percent / 100
    return float(amount - fee)