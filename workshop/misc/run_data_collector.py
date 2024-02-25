"""
To demonstrate how to use the python-binance library to download order books periodically.
https://python-binance.readthedocs.io/en/latest/index.html

To install the library: pip install python-binance

"""

import time
from common.config_logging import get_file_logger
from binance.client import Client


if __name__ == '__main__':
    logger = get_file_logger("depth", "/data/future_btcusdt.txt")
    client = Client()
    while True:
        depth = client.futures_order_book(symbol='BTCUSDT')
        print(depth)
        logger.info(depth)
        time.sleep(2)

