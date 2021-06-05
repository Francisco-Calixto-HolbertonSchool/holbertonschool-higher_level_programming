#!/usr/bin/python3
"""this module contains the base class of the project"""


from models.base import Base


class Rectangle(Base):
    """base class of the project"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor with optional instance id"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def eval_width(self):
        """useles coment"""
        return self.__width

    @eval_width.setter
    def eval_width(self, width):
        """useless comment """
        self.__width = width

    @property
    def eval_height(self):
        """useles coment"""
        return self.__height

    @eval_height.setter
    def eval_height(self, height):
        """useless comment """
        self.__height = height

    @property
    def eval_x(self):
        """useles coment"""
        return self.__x

    @eval_x.setter
    def eval_x(self, x):
        """useless comment """
        self.__x = x

    @property
    def eval_y(self):
        """useles coment"""
        return self.__y

    @eval_y.setter
    def eval_y(self, y):
        """useless comment """
        self.__y
