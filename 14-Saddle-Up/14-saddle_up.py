#!/usr/bin/env python3
"""
Module to perform matrix multiplication using NumPy.
"""
import numpy as np


def np_matmul(mat1, mat2):
    """
    Performs matrix multiplication on two numpy.ndarrays.

    Args:
        mat1 (numpy.ndarray): First matrix.
        mat2 (numpy.ndarray): Second matrix.

    Returns:
        numpy.ndarray: The resulting matrix product.
    """
    return mat1 @ mat2
