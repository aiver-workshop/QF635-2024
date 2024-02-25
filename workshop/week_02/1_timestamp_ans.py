"""
There are multiple ways to represent time, as float, as integer or datetime object.

In Python and generally computing context, a timestamp represents the number of seconds since EPOCH date (1970-01-01).
Computer timestamp is also known as epoch time.

Reference: https://realpython.com/python-time-module/

"""
import time
from datetime import datetime

# Get current time in seconds expressed as float
ts = time.time()

# Get current time in nanoseconds expressed as integer
tn = time.time_ns()

# print both timestamps
print(ts)
print(tn)

# convert epoc time to datetime obj
datetime_object = datetime.fromtimestamp(ts)
print(datetime_object)

