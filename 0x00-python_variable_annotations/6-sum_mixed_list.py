#!/usr/bin/env python3
"""
This module provides a function to sum a list containing both
integers and floats, returning the sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a mixed list containing
    both integers and floats.

    Parameters:
    mxd_lst (List[Union[int, float]]):
    A list containing integers and floats.

    Returns:
    float: The sum of the elements in the list.
    """
    return float(sum(mxd_lst))
