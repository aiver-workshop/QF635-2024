"""
Create a pricing strategy that always maintain a buy and sell order in the market to capture the spread:
    - Use a post-only buy order to quote on bid side
    - Use a post-only sell order to quote on ask side
    - keep track of net position

Main consideration:
    - At which price level should we place our orders?
    - How do we ensure that we only have at max one order on each side of the order book?
    - How sensitive is our pricing i.e. when should we refresh our price when market moves?
    - To update our price, should we cancel previous before sending new order?
    - How do we keep track of our order in the market and its current status?

"""
import os
import time
from dotenv import load_dotenv
from common.interface_book import VenueOrderBook
from common.interface_order import OrderEvent, Side, OrderStatus
from workshop.week_07.binance_gateway import BinanceFutureGateway
import logging

logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)


# TODO Pricing strategy class
class PricingStrategy:
    pass


if __name__ == '__main__':
    # get api key and secret
    dotenv_path = '/vault/binance_keys'
    load_dotenv(dotenv_path=dotenv_path)
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')

    # strategy parameters
    symbol = 'BTCUSDT'
    order_size = 0.01
    sensitivity = 0.1

    # create a binance gateway object
    binance_gateway = BinanceFutureGateway(symbol, api_key, api_secret)

    # create a strategy a register callbacks with gateway

    strategy = PricingStrategy(symbol, order_size, sensitivity, binance_gateway)
    binance_gateway.register_execution_callback(strategy.on_execution)
    binance_gateway.register_depth_callback(strategy.on_orderbook)

    # start
    binance_gateway.connect()
    strategy.start()

    while True:
        time.sleep(2)
