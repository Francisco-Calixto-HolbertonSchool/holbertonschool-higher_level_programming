#!/usr/bin/python3
"""This module contains Rectangle class"""


BaseGeometry =  __import__('7-base_geometry').BaseGeometry
"""import BaseGeometry"""


class Rectangle(BaseGeometry):
    """Rectangle class inherits from basegeometry"""

    """instantiation with dimensions"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        __width = 0
        __height = 0
