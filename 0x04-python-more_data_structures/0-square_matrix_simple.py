#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    
    cube = [list(map((lambda x: x * x), elm)) for elm in matrix]

    return cube
