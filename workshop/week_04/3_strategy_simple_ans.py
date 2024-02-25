"""
Create a simple strategy to buy and sell periodically.

"""
import logging
import os
import time
from dotenv import load_dotenv
from urllib.parse import urlencode
import hmac
import hashlib
import requests

# logging configuration
logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)

# URLs
BASE_URL = 'https://testnet.binancefuture.com'


# get api key and secret
def get_credentials():
    dotenv_path = '/vault/binance_keys'
    load_dotenv(dotenv_path=dotenv_path)
    # return api key and secret as tuple
    return os.getenv('BINANCE_API_KEY'), os.getenv('BINANCE_API_SECRET')


# send market order
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


# main loop to buy and sell periodically
if __name__ == '__main__':
    # get api key and secret
    api_key, api_secret = get_credentials()

    is_buy = True
    while True:
        send_market_order(api_key, api_secret, 'BTCUSDT', 0.1, is_buy)

        # sleep
        logging.info('sleep')
        time.sleep(10)

        # flip side
        is_buy = not is_buy

