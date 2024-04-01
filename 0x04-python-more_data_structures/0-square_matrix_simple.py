#!/usr/bin/python3
"""This script contains a function that initializes a matrix"""

def square_matrix_simple(matrix=[]):
    res = [list(map(lambda x: x ** 2, row)) for row in matrix]
    return res
