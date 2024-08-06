#!/usr/bin/env python3
"""Paralel Comprehensions task 2"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the time it takes to gather a coroutine four times"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    total = time.perf_counter() - start
    return total
