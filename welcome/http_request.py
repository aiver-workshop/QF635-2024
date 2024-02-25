"""
A simple program to request HTTP content, and write it to file. Later you can open the output html file in Chrome.

"""

import requests as http

response = http.get("https://en.wikipedia.org/wiki/Main_Page")
print(response.text)