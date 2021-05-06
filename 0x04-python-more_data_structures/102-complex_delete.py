#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    aux = a_dictionary.copy()
    for key in aux:
        if a_dictionary[key] == value:
            del a_dictionary[key]
    return a_dictionary
