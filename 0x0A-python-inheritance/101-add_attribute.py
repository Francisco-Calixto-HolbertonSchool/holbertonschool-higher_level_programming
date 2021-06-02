#!/usr/bin/python3
"""module commenting yomama"""


"""set atr atr"""
def add_attribute(obj, name, value):
    setattr(obj, name, value)
    if not hasattr(obj, name):
        raise TypeError("can't add new attribute")
