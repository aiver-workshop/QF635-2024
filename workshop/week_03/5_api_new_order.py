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
import os
import time
from dotenv import load_dotenv
from urllib.parse import urlencode
import hmac
import hashlib
import requests

# TODO load Testnet api key and secret from local file
API_KEY = None
API_SECRET = None

# TODO timestamp in milliseconds
timestamp = None

# TODO market order parameters
order_params = {
    'timestamp': timestamp
}

# TODO create query string
query_string = None
print('Query string: {}'.format(query_string))

# TODO signature
signature = None
print('Signature: {}'.format(signature))

# TODO Testnet URL - POST /fapi/v1/order
base_url = None
api_url = None
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

# TODO get order id from response data

# TODO use order id to query order status and get filled price
