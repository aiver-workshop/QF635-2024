"""
Running your first program using a main

"""
from datetime import date

if __name__ == '__main__':
    today = date.today()
    print('Welcome to QF635: Market Microstructure & Algorithmic Trading')
    print("Today is {}, {}".format(today.strftime('%A'), today.strftime("%B %d, %Y")))
    print('5 + 3 = {}'.format(5+3))
