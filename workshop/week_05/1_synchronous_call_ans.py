"""
A synchronous call invokes a method, wait for it to completes execution before returning a result to the caller.
No other method can run during the execution of the method.

A method is synchronous by default

"""
import time
import logging

logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)


# define a method to calculate factorial, and sleep for 1 second during each multiply step
def factorial(n: int) -> int:
    _result = 1
    logging.info("Start factorial calculation for n=" + str(n))
    for i in range(1, n+1):
        # sleep for a second
        time.sleep(1)

        logging.info('Calculating factorial[{}] step = {}'.format(n, i))

        # multiply factorial value
        _result = _result * i

    return _result


# we run the method twice, and note that the method executes sequentially requiring 25 (10 + 15) seconds in total
if __name__ == '__main__':
    logging.info('Factorial of 10 = {}'.format(factorial(10)))
    logging.info('Factorial of 15 = {}'.format(factorial(15)))
