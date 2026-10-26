"""Refund calculation for the payment service.

This module provides a utility function to compute the refundable amount
after applying a service fee expressed as a percentage of the original
transaction amount.
"""

def calculate_refund(amount, fee_percent=15):
    """Return the refund amount after deducting the service fee.

    Args:
        amount (float or int): The original transaction amount.
        fee_percent (float or int, optional): The service fee expressed as a
            percentage of ``amount``. Defaults to ``15`` (i.e., 15%).

    Returns:
        float: The amount remaining after the fee has been deducted.

    The fee is calculated as ``amount * fee_percent / 100``. For example,
    ``calculate_refund(100)`` returns ``85.0`` because a 15 % fee on 100 is
    15, leaving 85.
    """
    # Validate input types
    if not isinstance(amount, (int, float)):
        raise TypeError("amount must be a number")
    if not isinstance(fee_percent, (int, float)):
        raise TypeError("fee_percent must be a number")

    # Correct fee calculation: percentage of the amount
    fee = amount * fee_percent / 100
    return amount - fee