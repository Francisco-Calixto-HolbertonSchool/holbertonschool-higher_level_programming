#!/usr/bin/python3
"""This module contains an empty class that defines a rectangle"""


class Rectangle:
    """Class defines rectangle, for now does nothing"""
    __width = 0
    __height = 0

    """Instantiation with optional width and height"""
    def __init__(self, width=0, height=0):
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    """width retriever"""
    @property
    def width(self):
        return self.__width

    """width setter"""
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    """height retriever"""
    @property
    def height(self):
        return self.__height

    """height setter"""
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """returns area of rectangle"""
    def area(self):
        return (self.__width * self.__height)

    """return perimeter of rectangle, 0 if any side is 0"""
    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return ((self.__width + self.__height) * 2)
