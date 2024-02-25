"""
Dictionaries are used to store data values in (key:value) pairs. Also known as map.

Use a dictionary to store bids and asks price:size of an order book. Sort to get top-of-book prices.

Reference: https://docs.python.org/3/howto/sorting.html
"""

bids = {}
asks = {}

# add the following price/size to bids side: (12.5, 5), (15.2, 4), (11.8, 3)
bids[12.5] = 5
bids[15.2] = 4
bids[11.8] = 3

# add the following price/size to asks side: (24.7, 6), (21.5, 4), (22.1, 1)
# TODO

# use sorted() to sort bids in descending order to print best price (15.2)
# TODO

# use sorted() to sort asks in ascending order to print best price (21.5)
# TODO

# compute mid
# TODO
