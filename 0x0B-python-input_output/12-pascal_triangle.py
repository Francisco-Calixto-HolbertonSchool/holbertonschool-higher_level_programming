#!/usr/bin/python3
"""modules containing that reads text and prints"""


def pascal_triangle(n):
    """write text to file, overwrite if needed"""
    triangle = []
    if n <= 0:
        return []
    for i in range(n):
        a = 11 ** i
        row = [int(digit) for digit in str(a)]
        triangle += [row]
    return triangle
