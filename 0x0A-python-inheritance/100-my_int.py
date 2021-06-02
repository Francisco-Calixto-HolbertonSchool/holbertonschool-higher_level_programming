#!/usr/bin/python3
"""This module contains Mylist class"""


class MyInt(int):
    """aakakak kakakakk kk"""

    """reverter equality"""
    def __eq__(self, num):
        return (super().__ne__(num))

    """reverter inequality"""
    def __ne__(self, num):
        return (super().__eq__(num))
