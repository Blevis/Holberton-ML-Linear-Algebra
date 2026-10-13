#!/usr/bin/env python3

"""
Module to perform element-wise addition on two 2D matrices.
"""

def add_matrices2D(mat1, mat2):
    if len(mat1) != len(mat2):
        return None

    new_matrix = []
    for row1, row2 in zip(mat1, mat2):
        if len(row1) != len(row2):
            return None
        new_matrix.append([a + b for a, b in zip(row1, row2)])
        
    return new_matrix
