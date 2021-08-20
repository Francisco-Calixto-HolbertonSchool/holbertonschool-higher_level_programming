#!/usr/bin/python3
'''ends a POST request to the passed URL with the email as a parameter'''

import urllib.request
from sys import argv

if __name__ == "__main__":
    value = {"Your email is": argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(argv[1], data)
    with urllib.request.urlopen(req) as res:
        body = res.read()
    print(body.decode('utf-8'))
