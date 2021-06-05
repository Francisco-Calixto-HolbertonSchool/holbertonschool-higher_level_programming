#!/usr/bin/python3
"""this module contains the base class of the project"""


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
