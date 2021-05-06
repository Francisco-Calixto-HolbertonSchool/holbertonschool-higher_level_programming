#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    aux = []
    for i in a_dictionary:
        aux.append(i)
    maxi = aux[0]
    for j in aux:
        if a_dictionary[j] > a_dictionary[maxi]:
            maxi = j
    return maxi
