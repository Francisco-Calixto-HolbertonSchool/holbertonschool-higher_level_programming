#!/usr/bin/python3
def uniq_add(my_list=[]):
    set_aux = set(my_list)
    suma = 0
    for i in set_aux:
        suma += i
    return suma
