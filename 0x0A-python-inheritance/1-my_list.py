#!/usr/bin/python3
"""This module contains Mylist class"""


class MyList(list):
    """Class defines rectangle, for now does nothing"""

    """inheriting from list"""
    def __init__(self):
        super().__init__()

    """prints sorted list"""
    def print_sorted(self):
        cpy = self.copy()
        cpy.sort()
        print(cpy)
