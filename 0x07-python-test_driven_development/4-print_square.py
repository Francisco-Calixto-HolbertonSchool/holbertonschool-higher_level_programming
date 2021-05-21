#!/usr/bin/python3
"""contains a fucntion that prints magic squares"""


def print_square(size):
    """takes size as parameter nd prints equilateral square"""
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    area = size ** 2
    for i in range(1, area + 1):
        if i % size == 0:
            print('#')
        else:
            print('#', end="")
