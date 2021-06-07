#!/usr/bin/python3
"""this module contains the class square"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """base class of the project"""

    def __init__(self, size, x=0, y=0, id=None):
        """class contructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overwrite things dooo"""
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        """size prperty setter"""
        return self.width

    @size.setter
    def size(self, v):
        """size property ge"""
        self.width = v
        self.heiht = v
