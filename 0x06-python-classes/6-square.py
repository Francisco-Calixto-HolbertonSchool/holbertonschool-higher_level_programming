#!/usr/bin/python3
"""Square class defined by size and"""


class Square:
    """size validation"""

    def __init__(self, size=0, position=(0, 0)):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        if (isinstance(position, tuple) is False) or (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (isinstance(position[0], int) is False) or (isinstance(position[1], int) is False):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    """public class return area of square"""

    def area(self):
        return (self.__size ** 2)

    """retriever o"""

    @property
    def size(self):
        return self.__size

    """setter method"""

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    """instance to print square to stdout"""

    def my_print(self):
        lado = self.__size
        area = lado ** 2
        enter = self.__position[1]
        sep = self.__position[0]
        if lado == 0:
            print("")
        else:
            for ent in range(enter):
                print("")
            for sp in range(sep):
                print(" ", end='')
            for i in range(1, (area + 1)):
                if i % lado == 0:
                    print("#")
                    if i != area:
                        for s in range(sep):
                            print(" ", end='')
                else:
                    print("#", end="")

    """position retriever"""

    @property
    def position(self):
        return self.__position

    """position setter"""

    @position.setter
    def position(self, value):
        if (isinstance(position, tuple) is False) or (len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if (isinstance(position[0], int) is False) or (isinstance(position[1], int) is False):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
