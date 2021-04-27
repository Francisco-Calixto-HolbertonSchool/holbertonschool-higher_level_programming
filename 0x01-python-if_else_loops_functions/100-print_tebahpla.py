#!/usr/bin/python3
for c in reversed(range(97, 123)):
    asci = 0
    if c % 2 == 1:
        asci = 32
    print("{}".format(chr(c - asci)), end='')
