#!/usr/bin/python3
'''fetches https://intranet.hbtn.io/status'''

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        body = response.read()

    print(f"Body response:\n\
    \t- type: {type(body)}\n\
    \t- content: {body}\n\
    \t- utf8 content: {body.decode('utf8')}")
