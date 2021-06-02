#!/usr/bin/python3
"""modules containing that reads text and prints"""


import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""import jasonn utilities"""


def main():
    """main function"""
    new_args = []
    actual = load_from_json_file("add_item.json")
    for i in range(1, len(argv)):
        new_args.append(argv[i])
    new_lis = actual + new_args
    save_to_json_file(new_lis, "add_item.json")
