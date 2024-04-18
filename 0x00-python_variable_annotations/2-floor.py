#!/usr/bin/env python3
"""
This module provides a function to compute the floor of a floating-point number.
"""

import math

def floor(n: float) -> int:
    """
    Computes the floor of a floating-point number.

    Parameters:
    n (float): The number whose floor is to be calculated.

    Returns:
    int: The floor of the number, which is the largest integer less than or equal to n.
    """
    return math.floor(n)
