#!/user/bin/python3
"""Square class defined by size and verifies if size is valid"""


class Square:
    """Inside the class yeahhh"""
    __size = 0

    def __init__(self, size=0):
        """Functon to do everything"""
        if size is not None:
            self.__size = size
            if not isinstance(self.__size, int):
                raise TypeError('size must be an integer')
            if self.__size < 0:
                raise ValueError('size must be >= 0')
