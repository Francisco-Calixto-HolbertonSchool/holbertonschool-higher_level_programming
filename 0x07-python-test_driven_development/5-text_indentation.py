#!/usr/bin/python3
"""contains function that parses random string"""


def text_indentation(text):
    """searches for ? . or : in a string then prints newline"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for c in range(len(text)):
        if text[c] in ":.?":
            print(text[c])
            print("")
        else:
            print(text[c], end="")
