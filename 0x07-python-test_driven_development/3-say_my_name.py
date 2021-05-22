#!/usr/bin/python3
"""contains a function that takes name and las name and
prints with personalized message to stdout"""


def say_my_name(first_name, last_name=""):
    """This functions does what the decription above says"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
