import time

price = 100
size = 5

last_vwap_price = 0.0
last_vwap_size = 0.0

while True:

    # update vwap
    vwap_price = (last_vwap_price*last_vwap_size + price*size)/(last_vwap_size + size)

    print("vwap: {}".format(vwap_price))

    price += 1
    size += 1

    last_vwap_price = vwap_price
    last_vwap_size = last_vwap_size + size

    time.sleep(1)

