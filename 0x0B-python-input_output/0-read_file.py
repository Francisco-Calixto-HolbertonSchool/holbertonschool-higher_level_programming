#!/usr/bin/python3
"""modules containing that reads text and prints"""


def read_file(filename=""):
    """reads and prints from txt"""
    with open(filename, 'r', encoding="UTF8") as f:
        for line in f:
            print(line, end="")
