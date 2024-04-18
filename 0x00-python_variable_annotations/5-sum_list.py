#!/usr/bin/env python3
"""
This module provides a function to sum a list of floating-point numbers.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Sums a list of floating-point numbers and returns the total.

    Parameters:
    input_list (List[float]): A list of floating-point numbers to be summed.

    Returns:
    float: The sum of all elements in the list.
    """
    return sum(input_list)
