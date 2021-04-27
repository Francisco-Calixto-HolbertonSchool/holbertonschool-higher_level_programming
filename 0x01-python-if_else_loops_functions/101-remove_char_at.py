#!/usr/bin/pthon3
def remove_char_at(str, n):
    new = ""
    for c in range(0, len(str)):
        if c != n:
            new += str[c]
    return (new)
