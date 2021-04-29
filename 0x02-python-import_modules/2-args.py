#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    l = len(argv)
    if l == 1:
        print("0 arguments.")
    elif l == 2:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(l - 1))
        for i in range(1, l):
            print("{}: {}".format(i, argv[i]))
