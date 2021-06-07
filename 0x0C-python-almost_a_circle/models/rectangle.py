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

    def area(self):
        """area method"""
        return (self.width * self.height)

    def display(self):
        """print rectangle with #'s"""
        ancho = self.width
        alto = self.height
        area = alto * ancho
        space = self.x
        enter = self.y
        for e in range(enter):
            print('')
        for i in range(1, (area + 1)):
            if i % ancho == 1:
                for s in range(space):
                    print(' ', end='')
            if i % ancho == 0:
                print("#")
            else:
                print("#", end="")

    def __str__(self):
        """change the str"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            l = len(args)
            self.id = args[0]
            i = 1
            if i < l:
                self.width = args[i]
                i += 1
            if i < l:
                self.height = args[i]
                i += 1
            if i < l:
                self.x = args[i]
                i += 1
            if i < l:
                self.y = args[i]
        elif kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """to ionar ydicto"""
        dic = {}
        dic['id'] = self.id
        dic['width'] = self.width
        dic['height'] = self.height
        dic['x'] = self.x
        dic['y'] = self.y
        return dic
