"""
Lists are used to store multiple items in a single variable.
It is a collection which is ordered and changeable. Allows duplicate members.

We can use a list to store bid and ask prices of an order book
"""

# bid prices
bid_prices = [100, 99, 98]

# ask prices
ask_prices = [101, 103, 102]

# sort ask prices
ask_prices.sort()

# get best bid
best_bid = bid_prices[0]

# get best offer
best_offer = ask_prices[0]

# compute mid from best bid and offer
mid = 0.5 * (best_bid + best_offer)

# print mid
print(mid)
