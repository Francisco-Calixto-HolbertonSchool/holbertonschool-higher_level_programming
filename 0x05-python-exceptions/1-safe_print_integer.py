#!/usr/bin/python3
def safe_print_integer(value):
    flag = 1
    try:
        print("{:d}".format(value))
    except ValueError:
        flag = 0
    return (bool(flag))
