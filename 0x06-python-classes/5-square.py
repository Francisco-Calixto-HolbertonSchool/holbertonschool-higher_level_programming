#!/usr/bin/python3
"""Square class defined by size and"""


class Square:
    """size validation"""

    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
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
        if lado == 0:
            print("")
        else:
            for i in range(1, (area + 1)):
                if i % lado == 0:
                    print("#")
                else:
                    print("#", end="")
