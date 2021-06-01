#!/usr/bin/python3
"""This module contains Square class"""


Rectangle = __import__('9-rectangle').Rectangle
"""import Rectangle parent class"""


class Square(Rectangle):
    """Square class inherits from Rectangle"""

    """instantiation with size"""
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    """area of square"""
    def area(self):
        return (self.__size ** 2)

    """__str__"""
    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))
