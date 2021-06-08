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
        new = []
        filename = str(cls.__name__) + '.json'
        if list_objs is not None:
            for i in list_objs:
                new.append(cls.to_dictionary(i))
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(new))

    """static method"""

    @staticmethod
    def from_json_string(json_string):
        '''from json to string'''
        if json_string is None or len(json_string) == 0:
            return []
        return (json.loads(json_string))

    """class method"""

    @classmethod
    def create(cls, **dictionary):
        """create instance from dictionary"""
        dummy = cls(1, 1, 1, 1, 1)
        dummy.update(id=dictionary['id'], y=dictionary['y'], x=dictionary['x'],
                     height=dictionary['height'], width=dictionary['width'])
        return dummy
