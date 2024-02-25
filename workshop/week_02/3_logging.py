"""
Logging is a useful way to print useful information from a program, which can include the message timestamp.

Use logging module to print a series of increasing number once every 2 seconds.

Reference: https://realpython.com/python-logging/

"""

import logging

# configure output format to display timestamp
logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)

number = 1
while True:
    # log the number
    # TODO

    # stop execution for 2 seconds
    # TODO

    # increment the number
    number += 1
