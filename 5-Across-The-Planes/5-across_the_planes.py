#!/usr/bin/env python3

"""
Module to perform element-wise addition on two 2D matrices.
"""

def add_matrices2D(mat1, mat2):
    """
    Adds two 2D matrices element-wise.

    Args:
        mat1 (list of lists): First 2D matrix of ints/floats.
        mat2 (list of lists): Second 2D matrix of ints/floats.

    Returns:
        list of lists: A new 2D matrix with the element-wise sums, or None if shapes differ.
    """
    if len(mat1) != len(mat2):
        return None

    new_matrix = []
    for row1, row2 in zip(mat1, mat2):
        if len(row1) != len(row2):
            return None
        new_matrix.append([a + b for a, b in zip(row1, row2)])
        
    return new_matrix
