#!/usr/bin/pyhton3
"""modules containing that reads text and prints"""


def write_file(filename="", text=""):
    """write text to file, overwrite if needed"""
    with open(filename, 'w', encoding = "UTF8") as new_file:
        new_file.write(text)
    return (len(text))
