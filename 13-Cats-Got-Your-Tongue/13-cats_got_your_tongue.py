#!/usr/bin/env python3
"""
Module to concatenate two numpy arrays along a specific axis.
"""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """
    Concatenates two matrices along a specific axis.

    Args:
        mat1: First numpy-interpretable array.
        mat2: Second numpy-interpretable array.
        axis (int): Axis along which to concatenate.

    Returns:
        numpy.ndarray: A new concatenated numpy array.
    """
    return np.concatenate((mat1, mat2), axis=axis)
