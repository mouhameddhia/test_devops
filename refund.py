"""Refund calculation for the payment service.

Provides a utility to compute the refundable amount after applying a
service fee expressed as a percentage of the original amount.
"""

def calculate_refund(amount, fee_percent=15):
    """Return the refund amount after deducting the service fee.

    The ``fee_percent`` argument is interpreted as a percentage (e.g. ``15``
    means a 15 % fee). The function calculates the fee as ``amount *
    fee_percent / 100`` and subtracts it from the original amount.

    Parameters
    ----------
    amount : float or int
        The original amount to be refunded.
    fee_percent : float or int, optional
        The fee percentage to deduct from ``amount``. Defaults to ``15``.

    Returns
    -------
    float
        The amount remaining after the fee has been deducted.
    """
    fee = amount * fee_percent / 100
    return amount - fee