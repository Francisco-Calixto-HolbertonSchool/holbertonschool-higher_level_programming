#!/usr/bin/python3
"""this module contains the base class of the project"""


import json
"""import json"""


class Base():
    """base class of the project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor with optional instance id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    '''static method '''

    @staticmethod
    def to_json_string(list_dictionaries):
        """dictonary to json string"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return (json.dumps(list_dictionaries))

    '''class method'''

    @classmethod
    def save_to_file(cls, list_objs):
        """mi pan """

    """static method"""

    @staticmethod
    def from_json_string(json_string):
        '''from json to string'''
        if json_string is None or len(json_string) == 0:
            return []
        return (json.loads(json_string))
