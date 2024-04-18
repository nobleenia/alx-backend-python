#!/usr/bin/env python3
"""
This module provides a function that takes a string and a number (either int or float),
and returns a tuple. The tuple contains the string and the square of the number as a float.
"""

from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Accepts a string and a number, and returns a tuple. The tuple's first element is the
    string, and the second element is the square of the number converted to float.

    Parameters:
    k (str): The string component of the tuple.
    v (Union[int, float]): The numerical component of the tuple, to be squared.

    Returns:
    Tuple[str, float]: A tuple containing the string and the square of the number as a float.
    """
    return (k, float(v**2))
