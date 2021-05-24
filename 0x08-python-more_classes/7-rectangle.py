#!/usr/bin/python3
"""This module contains an empty class that defines a rectangle"""


class Rectangle:
    """Class defines rectangle, for now does nothing"""
    __width = 0
    __height = 0
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    """method to print rectangle using str()"""
    def __str__(self):
        ancho = self.__width
        area = self.__width * self.__height
        rect = ""
        symbol = str(self.print_symbol)
        for i in range(1, area + 1):
            if i % ancho == 0 and i != area:
                rect += symbol
                rect += '\n'
            else:
                rect += symbol
        return rect

    """method to print goodbye message when instance is deleted"""
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
