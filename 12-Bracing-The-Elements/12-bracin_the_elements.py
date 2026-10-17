#!/usr/bin/env python3
"""
Module to perform element-wise operations on numpy arrays.
"""


def np_elementwise(mat1, mat2):
    """
    Performs element-wise addition, subtraction, multiplication, and division.

    Args:
        mat1: First numpy-interpretable array or scalar.
        mat2: Second numpy-interpretable array or scalar.

    Returns:
        tuple: A tuple containing the sum, difference, product, and quotient.
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
