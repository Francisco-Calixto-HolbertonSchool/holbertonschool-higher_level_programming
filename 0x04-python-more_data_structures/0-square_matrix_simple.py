#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ]
    sq = matrix.copy()
    for r in range(len(matrix)):
        sq[r] = list(map(square, matrix[r]))
    return sq

def square(item):
    return item ** 2
