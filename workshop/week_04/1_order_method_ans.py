"""

Create a method to send market order

"""

import logging
import time
from urllib.parse import urlencode
import hmac
import hashlib
import requests

logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)

# Base URLs
BASE_URL = 'https://testnet.binancefuture.com'


def send_market_order(key: str, secret: str, symbol: str, quantity: float, side: bool):
    # order parameters
    timestamp = int(time.time() * 1000)
    params = {
        "symbol": symbol,
        "side": "BUY" if side else "SELL",
        "type": "MARKET",
        "quantity": quantity,
        'timestamp': timestamp
    }

    # create query string
    query_string = urlencode(params)
    logging.info('Query string: {}'.format(query_string))

    # signature
    signature = hmac.new(secret.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256).hexdigest()

    # url
    url = BASE_URL + '/fapi/v1/order' + "?" + query_string + "&signature=" + signature

    # post request
    session = requests.Session()
    session.headers.update(
        {"Content-Type": "application/json;charset=utf-8", "X-MBX-APIKEY": key}
    )
    response = session.post(url=url, params={})

    # get order id
    response_map = response.json()
    order_id = response_map.get('orderId')

    return order_id


if __name__ == '__main__':
    api_key = ''
    api_secret = ''
    send_market_order(api_key, api_secret, 'BTCUSDT', 0.1, True)
