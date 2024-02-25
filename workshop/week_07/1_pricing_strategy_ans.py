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


# An order class with status information
class Order:
    def __init__(self, symbol: str, side: Side, price, quantity, tif='IOC'):
        self.symbol = symbol
        self.side = side
        self.price = price
        self.quantity = quantity
        self.tif = tif
        self.last_order_event = None
        self.cancelling = False


# Pricing strategy class
class PricingStrategy:

    def __init__(self, symbol: str, order_size, sensitivity, binance_gateway: BinanceFutureGateway):
        self._symbol = symbol
        self._order_size = order_size
        self._sensitivity = sensitivity
        self._binance_gateway = binance_gateway
        self._position = 0
        self._live_buy_order = None
        self._live_sell_order = None

    def start(self):
        logging.info("Start strategy")

    # callback on order book update
    def on_orderbook(self, order_book: VenueOrderBook):
        # raise a buy order if there is currently none
        if self._live_buy_order is None:
            _limit_price = order_book.get_book().get_best_bid()
            _order = Order(self._symbol, Side.BUY, _limit_price, self._order_size)
            self._post_only_order(_order)
        else:
            # should we refresh our price?
            if abs(order_book.get_book().get_best_bid() - self._live_buy_order.price) > self._sensitivity:
                # cancel live order
                self._cancel_order(self._live_buy_order)

        # raise a sell order if there is currently none
        if self._live_sell_order is None:
            _limit_price = order_book.get_book().get_best_ask()
            _order = Order(self._symbol, Side.SELL, _limit_price, self._order_size)
            self._post_only_order(_order)
        else:
            # should we refresh our price?
            if abs(order_book.get_book().get_best_ask() - self._live_sell_order.price) > self._sensitivity:
                # cancel live order
                self._cancel_order(self._live_sell_order)

    # callback on execution update
    def on_execution(self, order_event: OrderEvent):
        logging.info("Receive execution: {}".format(order_event))
        self._update_position(order_event)

        if order_event.side == Side.BUY:
            if self._live_buy_order:
                self._live_buy_order.last_order_event = order_event
                if self._is_complete(order_event):
                    # buy order is done, we can create new one
                    self._live_buy_order = None
        else:
            if self._live_sell_order:
                self._live_sell_order.last_order_event = order_event
                if self._is_complete(order_event):
                    # sell order is done, we can create new one
                    self._live_sell_order = None

    def _post_only_order(self, order: Order):
        if order.side == Side.BUY:
            # ensure there's no existing buy order
            if self._live_buy_order is None:
                success = self._binance_gateway.place_limit_order(order.side, order.price, order.quantity, 'GTX')
                if success:
                    self._live_buy_order = order
            else:
                raise Exception("Logic error - attempt to raise buy order when there is already one")
        else:
            # ensure there's no existing sell order
            if self._live_sell_order is None:
                success = self._binance_gateway.place_limit_order(order.side, order.price, order.quantity, 'GTX')
                if success:
                    self._live_sell_order = order

    # cancel the given order if not cancel request not previously sent
    def _cancel_order(self, order: Order):
        if not self._ready_to_cancel(order):
            # not ready to cancel yet, wait
            return
        if not order.cancelling:
            _order_id = order.last_order_event.order_id
            logging.info("Sending cancel request for order id: {}".format(_order_id))
            order.cancelling = self._binance_gateway.cancel_order(order.symbol, order.last_order_event.order_id)

    # update current position
    def _update_position(self, order_event: OrderEvent):
        _sign = 1 if order_event.side == Side.BUY else -1
        self._position += (_sign * order_event.last_filled_quantity)
        logging.info("Net position: {:.3f}".format(self._position))

    # check if order has completed
    def _is_complete(self, order_event: OrderEvent):
        return order_event.status == OrderStatus.FILLED or \
            order_event.status == OrderStatus.PARTIALLY_FILLED or \
            order_event.status == OrderStatus.CANCELED or \
            order_event.status == OrderStatus.FAILED

    # check if order is ready to cancel
    def _ready_to_cancel(self, order: Order):
        return order.last_order_event is not None and not self._is_complete(order.last_order_event)


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
