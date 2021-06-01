#!/usr/bin/python3
"""This module contains declaration of function lookup"""

"""is passed an object which is searched for all attributes"""
def lookup(obj):
    ins = obj()
    lis = []
    for a in dir(ins):
        lis.append(a)
    return lis
