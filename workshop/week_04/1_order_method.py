"""

Create a method to send market order. User will specify the following parameters:
    - api key
    - api secret
    - price
    - size
    - side (True=buy, False=sell)

"""


# TODO
def send_market_order(key: str, secret: str, symbol: str, quantity: float, side: bool):
    pass


if __name__ == '__main__':
    api_key = ''
    api_secret = ''
    send_market_order(api_key, api_secret, 'BTCUSDT', 0.1, True)
