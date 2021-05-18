#!/user/bin/python3
"""Square class defined by size and verifies if size is valid"""


class Square:
    """Inside the class yeahhh"""
    __size = 0

    def __init__(self, size=0):
        """Functon to do everything"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
