#!/usr/bin/env python3
"""Basic annotations task 8"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function
    """
    def mult_fn(m):
        """Multiplies a float by another float
        """
        return m * multiplier
    return mult_fn
