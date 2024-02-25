"""
In Python asyncio, we can await on coroutines and tasks (also futures).

Awaiting on coroutines to run the methods sequentially (i.e. just like normal method call, each method will complete
execution before returning, this is also known as blocking call).

In next exercise, we will learn how to run multiple coroutines in parallel by awaiting on tasks.

"""
import asyncio
import logging

logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)


async def cut_ingredients():
    logging.info("Cutting ingredients...")
    await asyncio.sleep(2)
    logging.info("Finished cutting ingredients")


# TODO copy code from above and change the print, sleep for 5 seconds in between print
async def cook_food():
    pass


# TODO copy code from above and change the print, sleep for 10 seconds in between print
async def prepare_dessert():
    pass


async def cook():
    await cut_ingredients()
    await cook_food()
    await prepare_dessert()

if __name__ == '__main__':
    # run the async function by main thread
    asyncio.run(cook())
