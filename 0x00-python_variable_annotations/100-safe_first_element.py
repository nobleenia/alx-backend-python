#!/usr/bin/env python3
"""
Duck typing - first element of a sequence
"""

from typing import Any, Sequence, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of a sequence or None if the sequence is empty.

    Parameters:
    lst (Sequence[Any]): A sequence where the type of elements is not specified.

    Returns:
    Optional[Any]: The first element of the sequence or None if it is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
