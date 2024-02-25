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

"""
import logging
import os
import time
from dotenv import load_dotenv
from common.config_logging import to_stdout
from gateways.binance2.binance2 import BinanceGateway, ProductType

if __name__ == '__main__':
    to_stdout()

    # read key and secret from environment variable file
    dotenv_path = '/vault/binance_keys'
    load_dotenv(dotenv_path=dotenv_path)
    API_KEY = os.getenv('BINANCE_API_KEY')
    API_SECRET = os.getenv('BINANCE_API_SECRET')

    contract = 'BTCUSDT'
    binance = BinanceGateway(symbol=contract,  api_key=API_KEY, api_secret=API_SECRET, product_type=ProductType.FUTURE)
    binance.connect()

    while True:
        time.sleep(2)

        if binance.not_ready():
            logging.info("Not ready to trade")
        else:
            logging.info('Depth: %s' % binance.get_order_book(contract))
