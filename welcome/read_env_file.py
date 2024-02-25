"""
You should NEVER hardcode any sensitive information such as password in Python script.
A safer way to handle credential is saving them in a local file and load as environment variables.
There are more secure ways to manage secrets such as using Secret Manager service by cloud providers.
Students are encourage to explore further.

Use Notepad to create a ".my_secret" file under directory /vault to store <key>=<value> pairs, for example:
key=abc
secret=123

Note: If your computer is compromised, then potentially your secret files are exposed too.
"""

import os
from dotenv import load_dotenv

dotenv_path = '/vault/mysecret.txt'
load_dotenv(dotenv_path=dotenv_path)
my_username = os.getenv('NAME')
my_password = os.getenv('AGE')

print(my_username)
print(my_password)
