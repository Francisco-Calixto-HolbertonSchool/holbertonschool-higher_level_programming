#!/usr/bin/python3
"""modules containing that reads text and prints"""


import json
"""import jasonn gg"""


def load_from_json_file(filename):
    """write text to file, overwrite if needed"""
    with open(filename, 'r') as f:
        return (json.loads(f.read()))
