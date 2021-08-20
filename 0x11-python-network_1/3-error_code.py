#!/usr/bin/python3
'''httperror managing'''

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    from sys import argv

    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
