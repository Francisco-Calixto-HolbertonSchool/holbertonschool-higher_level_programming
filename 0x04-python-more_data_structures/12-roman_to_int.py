#!/usr/bin/python3
def roman_to_int(roman_string):
    if (not isinstance(roman_string, str)) or roman_string is None:
        return 0
    dic = {'X': 10, 'I': 1, 'C': 100, 'M': 1000, 'V': 5,
           'L': 50, 'D': 500, 'O': 0}
    suma = 0
    i = 0
    aux = []
    for c in roman_string:
        aux.append(c)
    aux.append('O')
    while dic[aux[i]] != 0:
        if dic[aux[i]] >= dic[aux[i + 1]]:
            suma += dic[aux[i]]
        else:
            suma -= dic[aux[i]]
        i += 1
    return suma
