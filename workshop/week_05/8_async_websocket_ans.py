"""
Listen to aggregate trade stream - https://binance-docs.github.io/apidocs/futures/en/#aggregate-trade-streams

"""

import websockets
import asyncio
import logging

logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)


URL = 'wss://fstream.binance.com/ws/bnbusdt@aggTrade'


# an async method to connect to WebSocket
async def subscribe():
    conn = websockets.connect(URL)
    ws = await conn.__aenter__()
    while ws.open:
        resp = await ws.recv()
        logging.info(resp)


# equivalent to above
async def subscribe2():
    async with websockets.connect(URL) as ws:
        while ws.open:
            resp = await ws.recv()
            logging.info(resp)


# run the subscription
asyncio.run(subscribe2())
