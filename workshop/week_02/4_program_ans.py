"""
Python interpreter executes a Python script from the top of the file when you run on it, or when the script
is imported as a module.

Like most other programming languages, a 'main' function defines a program starting point and is useful to
better understand the flow of a program. All the logics in the main function is executed only when run as a program
and not executed when imported as a module.

Reference: https://realpython.com/if-name-main-python/

"""
import time
import logging

logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)

# A simple program that prints a number from 1 to 10 once per second
if __name__ == '__main__':
    number = 1
    while True:
        # log the number
        logging.info(number)

        # stop execution for 2 seconds
        time.sleep(1)

        # increment the number
        number = number + 1
