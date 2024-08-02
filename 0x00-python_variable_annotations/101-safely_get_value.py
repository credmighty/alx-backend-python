#!/usr/bin/env python3
"""Basic annotations task 10"""
from typing import Union, Any, Mapping, TypeVar
T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """Checks if key exists in a dictionary
    """
    if key in dct:
        return dct[key]
    else:
        return default
