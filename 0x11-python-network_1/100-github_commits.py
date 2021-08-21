#!/usr/bin/python3
'''request url and get variable'''

import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    user = argv[2]
    url = "https://api.github.com/repos/" + user + '/' + repo + "/commits"
    response = requests.get(url)
    for i in range(10):
        try:
            sha = response.json()[i].get('sha')
            author = response.json()[i].get('commit').get('author').get('name')
            print("{}: {}".format(sha, author))
        except:
            break
