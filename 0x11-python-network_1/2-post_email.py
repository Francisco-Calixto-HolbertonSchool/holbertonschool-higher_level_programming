#!/usr/bin/python3
'''ends a POST request to the passed URL with the email as a parameter'''

import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    params = {'email' : argv[2]}
    data = urllib.parse.urlencode(params)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as res:
        body = res.read()
        print(body.decode('utf-8'))

