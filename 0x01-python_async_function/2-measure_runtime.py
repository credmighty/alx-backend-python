#!/usr/bin/env python3
"""2. measure runtime"""

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines.py').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
       a measure_time function with integers n and max_delay as arguments
       that measures the total execution time for wait_n(n, max_delay), and
       returns total_time / n. Your function should return a float.
    """

    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    total_time = end_time - start_time
    time_for_each_random_integer = total_time / n

    return time_for_each_random_integer
