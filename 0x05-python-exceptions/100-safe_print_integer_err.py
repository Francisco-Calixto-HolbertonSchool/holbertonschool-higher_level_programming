#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    flag = True
    try:
        print("{:d}".format(value))
    except Exception as err:
        print("Exception: {}".format(err), file=sys.stderr)
        flag = False
    return flag
