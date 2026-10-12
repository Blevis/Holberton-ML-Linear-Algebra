#!/usr/bin/env python3
"""
Module to transpose a 2D matrix.
"""


def matrix_transpose(matrix):
    """
    Returns the transpose of a 2D matrix.

    Args:
        matrix (list of lists): The 2D matrix to be transposed.

    Returns:
        list of lists: A new 2D matrix that is the transpose of the input.
    """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
