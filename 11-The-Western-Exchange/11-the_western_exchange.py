#!/usr/bin/env python3
"""
Module to transpose a numpy.ndarray.
"""


def np_transpose(matrix):
    """
    Transposes a numpy.ndarray.

    Args:
        matrix (numpy.ndarray): The numpy array to transpose.

    Returns:
        numpy.ndarray: A new transposed numpy array.
    """
    return matrix.T
