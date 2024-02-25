"""
Logging is a useful way to print useful information from a program, which can include the message timestamp.

Use logging module to print a series of increasing number once every 2 seconds.

Reference: https://realpython.com/python-logging/

"""

import logging
import time

# configure output format to include timestamp, thread name and logging level
logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)

number = 1
while True:
    # log the number
    logging.info(number)

    # stop execution for 2 seconds
    time.sleep(2)

    # increment the number
    number = number + 1
