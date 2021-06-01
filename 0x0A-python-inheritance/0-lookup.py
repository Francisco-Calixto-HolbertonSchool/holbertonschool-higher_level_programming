#!/usr/bin/python3
"""This module contains declaration of function lookup"""


def lookup(obj):
    """commenting my function for the checker"""
    ins = obj()
    lis = []
    for a in dir(ins):
        lis.append(a)
    return lis
