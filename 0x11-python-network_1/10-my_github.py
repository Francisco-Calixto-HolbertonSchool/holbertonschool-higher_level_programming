#!/usr/bin/python3
'''request url and get variable'''

import requests
from sys import argv

if __name__ == "__main__":
    params = {'read': 'user'}
    token = "token " + argv[2]
    authen = {'Authorization': token}
    url = 'https://api.github.com/users/' + argv[1]
    response = requests.get(url, headers=authen, data=params)
    print(response.json().get('id'))
