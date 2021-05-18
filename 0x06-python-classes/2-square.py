#!/user/bin/python3
class Square:
    __size = 0
    def __init__(self, size=0):
        if size is not None:
            self.__size = size
            if not isinstance(self.__size, int):
                raise TypeError('size must be an integer')
            if self.__size < 0:
                raise ValueError('size must be >= 0')
