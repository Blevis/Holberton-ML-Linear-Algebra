#!/usr/bin/env python3
"""
Module to concatenate two 2D matrices along a specific axis.
"""


def cat_matrices2D(mat1, mat2, axis=0):
    """
    Concatenates two 2D matrices along a specific axis.

    Args:
        mat1 (list of lists): First 2D matrix.
        mat2 (list of lists): Second 2D matrix.
        axis (int): Axis along which to concatenate (0 for rows, 1 for columns).

    Returns:
        list of lists: A new concatenated 2D matrix, or None if shapes differ.
    """
    if axis == 0:
        if mat1 and mat2 and len(mat1[0]) != len(mat2[0]):
            return None
        return [row[:] for row in mat1] + [row[:] for row in mat2]
    elif axis == 1:
        if len(mat1) != len(mat2):
            return None
        return [row1[:] + row2[:] for row1, row2 in zip(mat1, mat2)]
    return None
