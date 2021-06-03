#!/usr/bin/python3
"""modules containing that reads text and prints"""


def append_after(filename="", search_string="", new_string=""):
    """write text to file, overwrite if needed"""
    with open(filename, 'r') as f:
        opened = f.readline()

    with open(filename, 'w') as fil:
        s = ''
        for line in opened:
            s += line
            if search_string in line:
                s += new_string
        fil.write(s)
