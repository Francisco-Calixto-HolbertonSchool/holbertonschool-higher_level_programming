#!/usr/bin/python3
"""modules containing that reads text and prints"""


import json
"""import jasonn gg"""


def save_to_json_file(my_obj, filename):
    """write text to file, overwrite if needed"""
    with open(filename, 'w') as json_f:
        json_f.write(json.dumps(my_obj))
