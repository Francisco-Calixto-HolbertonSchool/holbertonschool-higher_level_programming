#!/usr/bin/python3
def weight_average(my_list=[]):
    total_participants = 0
    total_weight = 0
    if not my_list:
        return 0
    for tup in my_list:
        total_participants += tup[1]
        total_weight += (tup[0] * tup[1])
    final = total_weight / total_participants
    return final
