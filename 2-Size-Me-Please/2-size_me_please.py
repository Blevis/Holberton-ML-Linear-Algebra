#!/usr/bin/env python3
"""
Module to calculate the shape of a matrix.
"""


def matrix_shape(matrix):
    """
    Calculates the shape of a matrix.

    Args:
        matrix (list): A list or nested list representing the matrix.

    Returns:
        list: A list of integers representing the shape of the matrix.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        if len(matrix) > 0:
            matrix = matrix[0]
        else:
            break
    return shape
