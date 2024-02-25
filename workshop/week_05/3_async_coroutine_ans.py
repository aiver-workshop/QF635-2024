import asyncio
import time
import logging

logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)


# a normal (synchronous) method
def fetch_data():
    for i in range(3):
        print("[sync] fetching data " + str(i))
        time.sleep(1)
    return "data_a"


# A coroutine is a method with async keyword to indicate that its execution can be suspended before reaching return.
# Places where it can be suspended are the await statement.
async def fetch_data_async():
    for i in range(3):
        print("[asyncio] fetching data " + str(i))
        await asyncio.sleep(1)
    return "data_b"


if __name__ == '__main__':
    data = fetch_data()
    print(data)

    # run a coroutine
    data = asyncio.run(fetch_data_async())
    print(data)