#!/usr/bin/python3
def uppercase(str):
    for char in str:
        asci = 0
        if ord(char) >= 97 and ord(char) <= 122:
            asci = 32
        print("{}".format(chr(ord(char) - asci)), end="")
    print("")
