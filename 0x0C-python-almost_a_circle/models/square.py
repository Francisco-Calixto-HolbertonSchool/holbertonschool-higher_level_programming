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
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))

    @property
    def size(self):
        """size prperty setter"""
        return self.width

    @size.setter
    def size(self, v):
        """size property ge"""
        self.width = v
        self.heiht = v

    def update(self, *args, **kwargs):
        """updates values of the Square instance from args or kwargs"""
        if args:
            l = len(args)
            self.id = args[0]
            i = 1
            if i < l:
                self.size = args[i]
                i += 1
            if i < l:
                self.x = args[i]
                i += 1
            if i < l:
                self.y = args[i]
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """to ionar ydicto"""
        dic = {}
        dic['id'] = self.id
        dic['size'] = self.size
        dic['x'] = self.x
        dic['y'] = self.y
        return dic
