import logging
import random
import asyncio
import time
from threading import Thread

logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)


def start():
    loop_thread = Thread(target=run_async_task, daemon=True, name='Async Thread')
    loop_thread.start()


def run_async_task():
    # create a new event loop to run task by the calling thread
    loop = asyncio.new_event_loop()

    # create task and add it to the event loop
    loop.create_task(print_forever())

    # run the event loop until stop() is called
    loop.run_forever()


async def print_forever():
    while True:
        logging.info(random.randint(0, 100))
        await asyncio.sleep(1)


if __name__ == '__main__':
    # start the background task
    start()
    while True:
        time.sleep(5)
        logging.info('sanity check')

