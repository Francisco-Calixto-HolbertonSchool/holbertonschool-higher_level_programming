#!/usr/bin/python3
'''request url and get variable'''

import requests
from sys import argv

if __name__ == "__main__":
    try:
        q = argv[1]
    except:
        q = ""
    params = {'q': q}
    request = requests.post('http://0.0.0.0:5000/search_user', data=params)
    try:
        j = request.json()
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')
    else:
        if request.json() != {}:
            print("[{}] {}".format(j.get('id'), j.get('name')))
        else:
            print("No result")
