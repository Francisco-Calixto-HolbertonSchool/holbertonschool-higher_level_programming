#!/usr/bin/python3
"""This module contains Rectangle class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""import BaseGeometry"""


class Rectangle(BaseGeometry):
    """Rectangle class inherits from basegeometry"""

    """instantiation with dimensions"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    """area method returns area duuuu"""
    def area(self):
        return (self.__width * self.__height)

    """__str__ method to return when str()"""
    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
