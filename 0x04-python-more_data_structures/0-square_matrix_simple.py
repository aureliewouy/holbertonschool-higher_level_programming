#!/usr/bin/python3
def square_by_two(num):
    num = num ** 2
    return num

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
            new_matrix.append(list(map(square_by_two, i)))
    return new_matrix
