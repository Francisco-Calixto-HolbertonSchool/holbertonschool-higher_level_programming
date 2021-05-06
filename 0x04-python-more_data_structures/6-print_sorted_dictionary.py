#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    aux = []
    for i in a_dictionary:
        aux.append(i)
        aux.sort()
    for item in aux:
        print("{}: {}".format(item, a_dictionary[item]))
