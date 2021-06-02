#!/usr/bin/python3
"""modules containing that reads text and prints"""


import json
from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
"""import jssasonn utilities"""


actual = load_from_json_file("add_item.json")
for i in range(1, len(argv)):
    actual.append(argv[i])
save_to_json_file(actual, "add_item.json")
