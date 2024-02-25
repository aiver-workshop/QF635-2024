"""
To run multiple coroutines concurrently, wrap the coroutines in tasks and await on them to finish.

"""
import sys
import logging
import asyncio

logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)


# async keyword defines an asynchronous method, or known as a coroutine
# in this method, you can call other async method by using the await keywords
# async methods are usually I/O calls such as reading files, database or internet connection (HTTP/REST/WebSocket)
# when we await on another coroutine to return a result, we effective allows other coroutines to run for the time being
async def cut_ingredients():
    logging.info("Cutting ingredients...")
    # asyncio.sleep is a coroutine that we can await on (i.e. release control for other codes to run while sleeping)
    # sleep() is often used to simulate some I/O time consuming task
    await asyncio.sleep(2)
    logging.info("Finished cutting ingredients")


async def cook_food():
    logging.info("Cooking food...")
    # TODO sleep for 5 seconds
    logging.info("Finished cooking food")


async def prepare_dessert():
    logging.info("Preparing dessert...")
    # TODO sleep for 10 seconds
    logging.info("Finished preparing dessert")


async def cook():
    logging.info("Start cooking...")

    # a task signal to asyncio to run the method as soon as it can
    task_1 = asyncio.create_task(cut_ingredients())
    # TODO create 2 more tasks to do cook_food() and prepare_dessert()

    # TODO await for tasks to complete
    await task_1

    logging.info("Finished cooking")

if __name__ == '__main__':
    # run the async function by main thread
    asyncio.run(cook())
