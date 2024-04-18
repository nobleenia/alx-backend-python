#!/usr/bin/env python3
"""
Description: Add annotations to the below function’s parameters and
                 return values with the appropriate types
Parameters: lst: Iterable[Sequence]
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples,
    each containing a sequence and its length.

    Parameters:
    lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples,
    each tuple containing a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
