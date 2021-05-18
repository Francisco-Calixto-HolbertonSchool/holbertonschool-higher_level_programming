#!/user/bin/python3
"""Square class defined by size and ve"""


class Square:
    """Inside the class yeahhh"""

    def __init__(self, size=0):
        typ = isinstance(size, int)
        if typ is False:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
