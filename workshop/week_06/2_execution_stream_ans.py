"""
We are going to subscribe to execution stream to receive order update.

In Binance case, the steps are:
    1. Make a REST call to get a "listenKey"
    2. Subscribe to WEBSOCKET user data stream with the "listenKey"

https://binance-docs.github.io/apidocs/futures/en/#user-data-streams

Trade update details:
https://binance-docs.github.io/apidocs/futures/en/#event-order-update

"""
import asyncio
import json
import logging
import os
import websockets
from binance import Client, AsyncClient, BinanceSocketManager
from dotenv import load_dotenv

logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)


def get_credentials():
    dotenv_path = '/vault/binance_keys'
    load_dotenv(dotenv_path=dotenv_path)
    # return api key and secret as tuple
    return os.getenv('BINANCE_API_KEY'), os.getenv('BINANCE_API_SECRET')


async def listen_user_data(key, secret, ):
    logging.info("Getting listen key")
    client = Client(api_key, api_secret, testnet=True)
    listen_key = client.futures_stream_get_listen_key()

    # websocket connection url to future testnet user data stream
    url = 'wss://stream.binancefuture.com/ws/' + listen_key

    # start websocket connection
    logging.info("Subscribing to user data stream")
    conn = websockets.connect(url)
    ws = await conn.__aenter__()
    while ws.open:
        _message = await ws.recv()
        #logging.info(_message)

        # convert to json
        _data = json.loads(_message)
        update_type = _data.get('e')

        if update_type == 'ORDER_TRADE_UPDATE':
            _trade_data = _data.get('o')
            _execution_type = _trade_data.get('x')
            _order_status = _trade_data.get('X')
            _last_filled_price = _trade_data.get('L')
            _last_filled_qty = _trade_data.get('l')
            logging.info("Fill info: executionType={}, orderStatus={}, lastFillPrice={}, lastFillQty={}".format(_execution_type, _order_status, _last_filled_price, _last_filled_qty))


if __name__ == '__main__':
    # get api key and secret
    api_key, api_secret = get_credentials()

    asyncio.run(listen_user_data(api_key, api_secret))

