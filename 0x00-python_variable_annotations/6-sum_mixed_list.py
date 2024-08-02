#!/usr/bin/env python3
"""Basic annotations task 6"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of every element in a list
    """
    return sum(mxd_lst)
