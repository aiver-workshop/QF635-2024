import asyncio
import logging

logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)


# an async version of factorial method with an internal sleep
async def factorial(n: int) -> int:
    _result = 1
    logging.info("Started calculation for n=" + str(n))
    for i in range(1, n+1):
        # asyncio.sleep is a coroutine that we can await on (i.e. release control for other codes to run while sleeping)
        await asyncio.sleep(1)

        logging.info('Calculating factorial[{}] step = {}'.format(n, i))

        # multiply factorial value
        _result = _result * i

    return _result


async def concurrent_calculation() -> []:
    # schedule two calls to run concurrently
    results = await asyncio.gather(factorial(10), factorial(15))

    # print the results
    logging.info('Factorial of 10 = {}'.format(results[0]))
    logging.info('Factorial of 15 = {}'.format(results[1]))

if __name__ == '__main__':
    asyncio.run(concurrent_calculation())




