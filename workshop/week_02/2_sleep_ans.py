"""
Use a while-loop and time.sleep() function to print an increasing series of number once every 2 seconds.

Reference: https://www.geeksforgeeks.org/sleep-in-python/

"""
import time

number = 1
while True:
    # print the number
    print(number)

    # stop execution for 2 seconds
    time.sleep(2)

    # increment the number
    number = number + 1
