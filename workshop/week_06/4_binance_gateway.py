"""
Develop an order gateway called BinanceFutureGateway that allows strategy to do the follow:
    - register callback to handle order book update - on_orderbook
    - register callback to handle execution update - on_execution
    - call connect() to start connection to Binance
    - place a post-only limit order

For simplicity, this gateway only need to support one symbol - BTCUSDT

"""
import os
import time
from dotenv import load_dotenv
from common.interface_book import VenueOrderBook, PriceLevel, OrderBook
import logging
from common.interface_order import OrderEvent, OrderStatus, ExecutionType, Side

logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)


# TODO
class BinanceFutureGateway:
    pass


# callback on order book update
def on_orderbook(order_book: VenueOrderBook):
    logging.info("Receive order book: {}".format(order_book))


# callback on execution update
def on_execution(order_event: OrderEvent):
    logging.info("Receive execution: {}".format(order_event))


if __name__ == '__main__':
    # get api key and secret
    dotenv_path = '/vault/binance_keys'
    load_dotenv(dotenv_path=dotenv_path)
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')

    # create a binance gateway object
    binance_gateway = BinanceFutureGateway('BTCUSDT', api_key, api_secret)

    # register callbacks
    binance_gateway.register_depth_callback(on_orderbook)
    binance_gateway.register_execution_callback(on_execution)

    # start connection
    binance_gateway.connect()

    send_order = True
    while True:
        time.sleep(2)

        if send_order:
            # place an order once
            binance_gateway.place_limit_order(Side.BUY, 25000, 0.1, 'GTX')
            send_order = False
