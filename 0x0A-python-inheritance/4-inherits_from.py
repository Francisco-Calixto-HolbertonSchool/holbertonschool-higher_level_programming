#!/usr/bin/python3
"""This module contains declaration of function inherits_from"""


def inherits_from(obj, a_class):
    if issubclass(obj.__class__, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
