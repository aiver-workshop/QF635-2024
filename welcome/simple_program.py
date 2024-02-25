"""
A simple program to produce factorial

"""

import math
import time

n = 0
while True:
    result = math.factorial(n)
    print('{}! = {}'.format(n, result))
    time.sleep(1)
    n = n + 1
