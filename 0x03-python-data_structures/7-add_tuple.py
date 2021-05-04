#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new = []
    a = []
    b = []
    for j in range(len(tuple_a)):
        a.append(tuple_a[j])
    if len(tuple_a) < 2:        
        for i in range(len(tuple_a), 2):
            a.append(0)
    for x in range(len(tuple_b)):
        b.append(tuple_b[x])
    if len(tuple_b) < 2:
        for f in range(len(tuple_b), 2):
            b.append(0)
    new.append(a[0] + b[0])
    new.append(a[1] + b[1])
    tup = tuple(new)
    return tup
