#!/usr/bin/env python3
"""
Description: Use mypy to validate the following piece of code
                 and apply any necessary changes.
Parameters: lst: Tuple, factor: int = 2
"""

from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Returns a new list where each element in the input tuple
    is repeated 'factor' times.
    
    Parameters:
    lst (Tuple[int, ...]): A tuple of integers.
    factor (int): The number of times each element should be repeated.

    Returns:
    List[int]: A list of integers where each element in the original
    tuple is repeated 'factor' times.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in
