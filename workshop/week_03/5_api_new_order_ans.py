"""
Open a paper trading account at Binance Futures Testnet: https://testnet.binancefuture.com/en/futures/BTCUSDT

After login in, there is an "API Key" tab at the bottom section where you will find API Key and API Secret.
Using Notepad or Notepad++, create a file with the following key-value pairs
and saved under directory /vault as "binance_keys"

    BINANCE_API_KEY=<API Key>
    BINANCE_API_SECRET=<API Secret>

Remember to keep these secret and do not share with anyone.

For further information:
https://www.binance.com/en/support/faq/how-to-test-my-functions-on-binance-testnet-ab78f9a1b8824cf0a106b4229c76496d

Reference: https://binance-docs.github.io/apidocs/futures/en/#new-order-trade
"""

import time
from urllib.parse import urlencode
import hmac
import hashlib
import requests


API_KEY = ''
API_SECRET = ''

# timestamp in milliseconds
timestamp = int(time.time() * 1000)

# market order parameters
order_params = {
    "symbol": "BTCUSDT",
    "side": "BUY",
    "type": "MARKET",
    "quantity": 0.1,
    "timestamp": timestamp,
    "recvWindow": 10000
}

# create query string
query_string = urlencode(order_params)
print('Query string: {}'.format(query_string))

# signature
signature = hmac.new(API_SECRET.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256).hexdigest()
print('Signature: {}'.format(signature))

# Testnet URL - POST /fapi/v1/order
base_url = 'https://testnet.binancefuture.com'
api_url = '/fapi/v1/order'
url = base_url + api_url + "?" + query_string + "&signature=" + signature
print('URL: {}'.format(url))

# POST new order request
session = requests.Session()
session.headers.update(
    {"Content-Type": "application/json;charset=utf-8", "X-MBX-APIKEY": API_KEY}
)
response = session.post(url=url, params={})

# if response status is NEW, verify position on web interface - https://testnet.binancefuture.com/en/futures/BTCUSDT
response_data = response.json()
print("Response: {}".format(response_data))

# get order id from response data
order_id = response_data['orderId']

# use order id to query order status and get filled price
timestamp = int(time.time() * 1000)
query_params = {
    "symbol": "BTCUSDT",
    "orderId": order_id,
    "timestamp": timestamp,
    "recvWindow": 10000
}
query_string = urlencode(query_params)
signature = hmac.new(API_SECRET.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256).hexdigest()
url = base_url + api_url + "?" + query_string + "&signature=" + signature
get_response = session.get(url=url, params={})
status_data = get_response.json()
print("Response: {}".format(status_data))
print("Filled price: {}".format(status_data['avgPrice']))
