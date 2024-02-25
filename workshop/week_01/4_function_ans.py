"""
Define a function to calculate mid from bid and offer prices
"""


def calculate_mid(bid_price: float, offer_price: float) -> float:
    return 0.5 * (bid_price + offer_price)


mid = calculate_mid(100.50, 101.80)
print(mid)
