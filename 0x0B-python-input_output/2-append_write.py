#!/usr/bin/python3
"""modules containing that reads text and prints"""


def append_write(filename="", text=""):
    """reads and prints from txt"""
    with open(filename, 'a', encoding = "UTF8") as new_file:
        new_file.write(text)
    return (len(text))
