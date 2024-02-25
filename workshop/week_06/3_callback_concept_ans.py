"""
Demonstrate the concept of callback in an event-driven structure

"""

import time
import random
import logging

logging.basicConfig(format='%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s', level=logging.INFO)


# A callback is a method that is invoked when there is an event or incoming data
# This will be the main triggering point of a strategy
def handle_number(number):
    logging.info("Receive number: {}".format(number))


# Registering the callback - messaging between gateway and strategy
callback_method = handle_number


# A form of this loop will exist inside a gateway
while True:
    time.sleep(1)

    # assume this random number comes from a "source" - it could be an exchange
    # equivalent to websocket receiving messages
    a = random.randint(1, 100)

    if callback_method:
        try:
            # notify strategy via callback
            callback_method(a)
        except:
            print("An exception occurred")

    else:
        print('no callback registered')

