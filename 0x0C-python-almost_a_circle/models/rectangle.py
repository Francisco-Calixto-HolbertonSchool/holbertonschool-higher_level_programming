#!/usr/bin/python3
"""this module contains the base class of the project"""


from models.base import Base


class Rectangle(Base):
    """base class of the project"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor with optional instance id"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """useles coment"""
        return self.__width

    @width.setter
    def width(self, v):
        """useless comment """
        if type(v) is not int:
            raise TypeError("width must be an integer")
        if v <= 0:
            raise ValueError("width must be > 0")
        self.__width = v

    @property
    def height(self):
        """useles coment"""
        return self.__height

    @height.setter
    def height(self, v):
        """useless comment """
        if type(v) is not int:
            raise TypeError("height must be an integer")
        if v <= 0:
            raise ValueError("height must be > 0")
        self.__height = v

    @property
    def x(self):
        """useles coment"""
        return self.__x

    @x.setter
    def x(self, v):
        """useless comment """
        if type(v) is not int:
            raise TypeError("x must be an integer")
        if v < 0:
            raise ValueError("x must be >= 0")
        self.__x = v

    @property
    def y(self):
        """useles coment"""
        return self.__y

    @y.setter
    def y(self, v):
        """useless comment """
        if type(v) is not int:
            raise TypeError("y must be an integer")
        if v < 0:
            raise ValueError("y must be >= 0")
        self.__y = v
