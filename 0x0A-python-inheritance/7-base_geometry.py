#!/usr/bin/python3
"""This module contains BaseGeometry class"""


class BaseGeometry(list):
    """Class BaseGeometry, for now does nothing"""

    """useless functoin that rasies execption message"""
    def area(self):
        raise Exception("area() is not implemented")

    """integer validator function"""
    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
