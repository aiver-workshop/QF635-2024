"""
To maintain a local order book, one is required to get a snapshot and apply order book deltas to it:
    https://binance-docs.github.io/apidocs/futures/en/#how-to-manage-a-local-order-book-correctly

The workflow is somewhat complex and easy to get wrong, so we use a library instead to leverage the work by others:

    https://python-binance.readthedocs.io/en/latest/websockets.html
    https://python-binance.readthedocs.io/en/latest/depth_cache.html
    https://python-binance.readthedocs.io/en/latest/binance.html#binance.depthcache.FuturesDepthCacheManager

"""
import asyncio
from binance import AsyncClient, BinanceSocketManager
from binance.depthcache import FuturesDepthCacheManager
import logging

logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)


async def listen_depth_forever(symbol):
    _client = await AsyncClient.create(testnet=True)

    _depth_cache_manager = FuturesDepthCacheManager(_client, symbol=symbol)

    async with _depth_cache_manager as _dcm_socket:
        while True:
            _depth = await _dcm_socket.recv()
            logging.info('Book bid={}, ask={}'.format(_depth.get_bids()[0], _depth.get_asks()[0]))


if __name__ == '__main__':
    _loop = asyncio.new_event_loop()
    _loop.create_task(listen_depth_forever('BTCUSDT'))
    _loop.run_forever()

