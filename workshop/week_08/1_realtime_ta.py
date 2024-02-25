"""
This is a demonstration of how to collect data in realtime and compute technical signal using dataframe library.

Given we maintain all historical data in memory, this is by no means efficient as memory will grow indefinitely
and the program may crash due to out-of-memory exception.

Students are encourage to explore an alternative solution if the timeseries can grow too large.

"""

import pandas as pd
import pandas_ta as ta
import time
import random

# a timeseries to collect all historical data
timeseries = {
    'timestamp': [],
    'close': [],
}

while True:
    # simulate a price, add to timeseries
    dt = pd.to_datetime(time.time(), unit='s')

    # TODO replace with binance code to get order book
    price = random.randint(70, 100)

    timeseries['timestamp'].append(dt)
    timeseries['close'].append(price)

    # turn into dataframe
    df = pd.DataFrame(timeseries)
    df.set_index('timestamp', inplace=True)

    # calculate technical indicators
    df['perc_return'] = ta.percent_return(df.close)
    df['rsi5'] = ta.rsi(df.close, length=5)

    # print
    print(df.tail(1))

    # get signal
    rsi_signal = df.iloc[-1]['rsi5']
    target_position = None
    if rsi_signal:
        # TODO compute target position
        print('we have a signal: {}'.format(rsi_signal))
    else:
        print('no signal yet')

    if target_position:
        # TODO calculate order quantity to send, place order
        pass

    time.sleep(1)

