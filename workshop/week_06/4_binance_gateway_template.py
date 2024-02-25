"""
Develop an order gateway called BinanceFutureGateway that allows strategy to do the follow:
    - register callback to handle order book update - on_orderbook
    - register callback to handle execution update - on_execution
    - call connect() to start connection to Binance
    - place a post-only limit order

For simplicity, this gateway only need to support one symbol - BTCUSDT

"""
import asyncio
import json
import os
import time
from threading import Thread
import websockets
from binance.depthcache import FuturesDepthCacheManager
from binance import AsyncClient, BinanceSocketManager
from dotenv import load_dotenv
from common.interface_book import VenueOrderBook, PriceLevel, OrderBook
import logging
from common.interface_order import OrderEvent, OrderStatus, ExecutionType, Side

logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)


class BinanceFutureGateway:

    def __init__(self, symbol: str, api_key=None, api_secret=None, name='Binance', testnet=True):
        self._api_key = api_key
        self._api_secret = api_secret
        self._exchange_name = name
        self._symbol = symbol
        self.testnet = testnet

        # binance async client
        self._client = None
        self._dcm = None  # depth cache, which implements the logic to manage a local order book
        self._dws = None  # depth async WebSocket session

        # depth cache
        self._depth_cache = None

        # this is a loop and dedicated thread to run all async concurrent tasks
        self._loop = asyncio.new_event_loop()
        self._loop_thread = Thread(target=self._run_async_tasks, daemon=True, name=name)

        # callbacks
        self._depth_callbacks = []
        self._execution_callbacks = []

    """
        Connect method to start exchange connection
    """
    def connect(self):
        logging.info('Initializing connection')

        self._loop.run_until_complete(self._reconnect_ws())

        logging.info("starting event loop thread")
        self._loop_thread.start()

    # an internal method to reconnect websocket
    async def _reconnect_ws(self):
        logging.info("reconnecting websocket")
        self._client = await AsyncClient.create(self._api_key, self._api_secret, testnet=self.testnet)

    # an internal method to runs tasks in parallel
    def _run_async_tasks(self):
        """ Run the following tasks concurrently in the current thread """
        self._loop.create_task(self._listen_depth_forever())
        self._loop.create_task(self._listen_execution_forever())
        self._loop.run_forever()

    # an internal async method to listen to depth stream
    async def _listen_depth_forever(self):
        pass

    # an internal async method to listen to user data stream
    async def _listen_execution_forever(self):
        pass

    """ 
        Get order book 
    """
    def get_order_book(self) -> VenueOrderBook:
        pass

    """
        Place a limit order
    """
    def place_limit_order(self, side: Side, price, quantity, tif='IOC'):
        pass

    """
        Cancel an order
    """
    def cancel_order(self, order_id):
        pass

    """ 
        Register a depth callback function that takes one argument: (book: VenueOrderBook) 
    """
    def register_depth_callback(self, callback):
        pass

    """ 
        Register an execution callback function that takes one argument, an order event: (event: OrderEvent) 
    """
    def register_execution_callback(self, callback):
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
