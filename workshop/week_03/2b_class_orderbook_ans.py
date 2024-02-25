"""
An order book is often modelled with bids and asks sides, with each side being an array of Tier objects.

A tier represents a price level, which consists of price, quantity and a quote identifier.

"""
from datetime import datetime


# Tier represents a price level with information of price, quantity and identifier in the order book
class Tier:
    def __init__(self, price: float, size: float, quote_id: str = None):
        self.price = price
        self.size = size
        self.quote_id = quote_id

    def __str__(self):
        return '({}, {}, {})'.format(self.price, self.size, self.quote_id)


# OderBook class to hold bids and asks, as an array of Tiers
class OrderBook:
    def __init__(self, _timestamp: float, _bids: [Tier], _asks: [Tier]):
        self.timestamp = _timestamp
        self.bids = _bids
        self.asks = _asks

    # method to get best bid
    def best_bid(self):
        return self.bids[0].price

    # method to get best ask
    def best_ask(self):
        return self.asks[0].price

    # method to get mid
    def mid(self):
        return 0.5 * (self.best_ask() + self.best_bid())

    # provide print output
    def __str__(self):
        string = 'Creation time: {} '.format(self.timestamp)
        string += ', Bids: '
        for tier in self.bids[:4]:
            string += str(tier) + " "

        string = string + ', Asks: '
        for tier in self.asks[:4]:
            string += str(tier) + " "

        return string


# bids is an array of Tier objects
bids = [Tier(100, 2, 'b0001'), Tier(99, 3, 'b0002'), Tier(98, 4, 'b0003')]

# asks is an array of Tier objects
asks = [Tier(101, 2, 'a0001'), Tier(102, 3, 'a0002'), Tier(103, 4, 'a0003')]

# construct an order book with the bids and asks tiers
order_book = OrderBook(datetime.now(), bids, asks)

# print the order book
print(order_book)

# get mid from order book method and print
print(order_book.mid())

# compute bid/ask spread from top-of book
spread = order_book.best_ask() - order_book.best_bid()
print(spread)
