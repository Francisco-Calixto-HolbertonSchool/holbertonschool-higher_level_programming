#!/usr/bin/python3
'''send request and displays value of X-Request-Id variable'''

import urllib.request
from sys import argv

req = urllib.request.Request(argv[1])
with urllib.request.urlopen(req) as response:
    value = response.info()
print(value['X-Request-Id'])
