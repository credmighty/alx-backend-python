#!/usr/bin/env python3
"""Basic annotations task 10"""
from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns first element in list if list exists
    else returns None.
    """
    if lst:
        return lst[0]
    else:
        return None
