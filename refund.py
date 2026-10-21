"""Refund calculation for the payment service."""


def calculate_refund(amount, fee_percent=15):
    """Return the refund amount after deducting the service fee."""
    fee = amount * fee_percent
    return amount - fee
