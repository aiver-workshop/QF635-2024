"""
REST stands for Representational State Transfer, is an application programming interface (API or web API)
for a client to interact with resources by web services. RESTful APIs are often implemented using the
Hypertext Transfer Protocol (HTTP) over internet.

An HTTP method tells the server what it needs to do to the resource. The following are four common HTTP methods:
    - GET: to get a resource/information from the server
    - POST: to send data to the server
    - PUT: to update existing resources on the server
    - DELETE: to remove the resource (e.g. to delete a record)

Make a REST call using requests module to Binance future exchange to get instruments static data:
https://binance-docs.github.io/apidocs/futures/en/#change-log

Reference: https://realpython.com/python-requests/

"""
import requests

# Base endpoint - https://binance-docs.github.io/apidocs/futures/en/#general-api-information
# TODO
URL = ''

# Exchange info method - https://binance-docs.github.io/apidocs/futures/en/#exchange-information
# TODO
METHOD = ''

# Send HTTP GET request
# TODO make a GET request using the requests library

# convert to JSON object by response.json()
# TODO

# print status, price and quantity precision of each symbol
# TODO
