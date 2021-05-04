#!/usr/bin/python3
def multiple_returns(sentence):
    aux = []
    aux.append(len(sentence))
    if not sentence:
        aux.append(None)
    else:
        aux.append(sentence[0])
    return aux[0], aux[1]
