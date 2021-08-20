#!/usr/bin/python3
'''send request and displays value of X-Request-Id variable'''

import urllib.request
from sys import argv

if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    with urllib.request.urlopen(req) as response:
        value = response.info()
    print(value.get('X-Request-Id'))
