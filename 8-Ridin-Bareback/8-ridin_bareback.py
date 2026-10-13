#!/usr/bin/env python3
"""
Module to perform matrix multiplication on two 2D matrices.
"""


def mat_mul(mat1, mat2):
    """
    Performs matrix multiplication on two 2D matrices.

    Args:
        mat1 (list of lists): First 2D matrix.
        mat2 (list of lists): Second 2D matrix.

    Returns:
        list of lists: A new 2D matrix resulting from the multiplication,
                       or None if the matrices cannot be multiplied.
    """
    if not mat1 or not mat1[0] or not mat2 or not mat2[0]:
        return None

    rows_mat1 = len(mat1)
    cols_mat1 = len(mat1[0])
    rows_mat2 = len(mat2)
    cols_mat2 = len(mat2[0])

    if cols_mat1 != rows_mat2:
        return None

    result = [[sum(a * b for a, b in zip(row, col))
               for col in zip(*mat2)]
              for row in mat1]

    return result
    