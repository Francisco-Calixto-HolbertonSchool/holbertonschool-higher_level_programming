#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    aux = []
    for i in range(len(my_list)):
        if i != idx:
            aux.append(my_list[i])
    my_list.clear()
    for j in aux:
        my_list.append(j)
    return my_list
