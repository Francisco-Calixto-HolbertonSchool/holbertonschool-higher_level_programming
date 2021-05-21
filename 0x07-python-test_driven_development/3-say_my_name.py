#!/usr/bin/python3
"""contains a function that takes name and las name and
prints with personalized message to stdout"""


def say_my_name(first_name, last_name=""):
    """This functions does what the decription above says"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
