#!/usr/bin/env python3
"""1. concurrent coroutine"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Async routine called wait_n that takes in 2 int arguments: max_delay and n.
    You will spawn wait_random n times with the specified max_delay.
    wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using
    sort() because of concurrency.
    """
    items = []
    delays = []

    for _ in range(n):
        items.append(asyncio.create_task(wait_random(max_delay)))

    # Create queue with results depending on the function have the result ready
    for item in asyncio.as_completed(items):
        delays.append(await item)
    return delays
