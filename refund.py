"""Refund calculation for the payment service.

This module provides a utility to compute the refundable amount after
deducting a service fee expressed as a percentage of the original
transaction amount.
"""

def calculate_refund(amount, fee_percent=15):
    """Return the refund amount after deducting the service fee.

    Args:
        amount (float or int): The original transaction amount.
        fee_percent (float or int, optional): The service fee expressed as a
            percentage of ``amount``. Defaults to ``15`` (i.e., 15%).

    Returns:
        float: The amount remaining after the fee has been subtracted.
    """
    # Convert the percentage to a proportion (e.g., 15% -> 0.15)
    fee = amount * (fee_percent / 100.0)
    return amount - fee