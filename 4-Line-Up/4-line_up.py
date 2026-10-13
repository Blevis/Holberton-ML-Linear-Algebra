#!/usr/bin/env python3
"""
Module to perform element-wise addition on two arrays.
"""


def add_arrays(arr1, arr2):
    """
    Adds two arrays element-wise.

    Args:
        arr1 (list): First list of ints/floats.
        arr2 (list): Second list of ints/floats.

    Returns:
        list: A new list with the element-wise sums, or None if shapes differ.
    """
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
