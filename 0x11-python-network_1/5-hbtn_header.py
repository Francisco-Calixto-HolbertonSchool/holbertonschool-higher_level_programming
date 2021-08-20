#!/usr/bin/python3
'''request url and get variable'''

import requests
from sys import argv

if __name__ == "__main__":
    response = requests.get(argv[1])
    print(response.headers['X-Request-Id'])
