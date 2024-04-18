#!/usr/bin/env python3
"""
This module provides a function that creates a multiplier function. The returned
function will multiply any float by a specified multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Generates a function that multiplies a float by a given multiplier.

    Parameters:
    multiplier (float): The float value that will be used as the multiplier.

    Returns:
    Callable[[float], float]: A function that takes a float and returns the result
                               of multiplying it by the multiplier.
    """
    def multiplier_func(value: float) -> float:
        return value * multiplier
    return multiplier_func
