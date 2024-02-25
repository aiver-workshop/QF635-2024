"""
Private endpoint is a channel to perform user-specific operation such as getting account balance or raising orders.

A signature is required to authenticate the request, follow this guide:
https://binance-docs.github.io/apidocs/futures/en/#signed-trade-and-user_data-endpoint-security

"""
import hmac
import hashlib
from urllib.parse import urlencode, quote

# Credentials - this is example for convenience, never store in script like this
api_key = ''
api_secret = ''

# Query parameters
timestamp = 1591702613943
params = {
    "symbol": "",
    "side": "",
    "type": "",
    "quantity": None,
    "price": "",
    "timeInForce": "",
    'recvWindow': None,
    'timestamp': timestamp
}

# Create query string - see https://www.urlencoder.io/python/, Encoding multiple parameters at once
query_string = urlencode(params)
print('Query string: {}'.format(query_string))

# Endpoints use HMAC SHA256 signatures. Use secret key as the key and query string as the value for the HMAC operation.
# see https://www.geeksforgeeks.org/hmac-keyed-hashing-message-authentication/
signature = hmac.new(api_secret.encode("utf-8"), query_string.encode("utf-8"), hashlib.sha256).hexdigest()
print('Signature: {}'.format(signature))

# expectation
match = signature == '3c661234138461fcc7a7d8746c6558c9842d4e10870d2ecbedf7777cad694af9'
print('Match: {}'.format(match))


