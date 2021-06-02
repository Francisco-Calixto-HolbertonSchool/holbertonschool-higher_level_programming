#!/usr/bin/python3
"""module commenting yomama"""


def add_attribute(obj, name, value):
    """funciton lpmm jjjj"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
