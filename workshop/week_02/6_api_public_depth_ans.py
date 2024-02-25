"""
REST requests can include query parameters that give the server more details about what needs to be done.

Make a REST call to Binance future exchange to get order book of BTCUSDT (by specifying a symbol parameter)

To pass parameter to GET method, look under section "Query String Parameters"
Reference: https://realpython.com/python-requests/

"""

import requests

# Base endpoint
URL = 'https://fapi.binance.com'

# https://binance-docs.github.io/apidocs/futures/en/#order-book
METHOD = '/fapi/v1/depth'

# GET request
response = requests.get(URL + METHOD, params={'symbol': 'BTCUSDT'})

# convert to JSON object by response.json()
order_book = response.json()

# print best bid and offer price
best_bid = order_book['bids'][0][0]
best_ask = order_book['asks'][0][0]

print('Best bid:{}, ask: {}'.format(best_bid, best_ask))
