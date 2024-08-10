#!/usr/bin/env python3
"""async basic - 4. task"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Take the code from wait_n and alter it into a new function task_wait_n.
    The code is nearly identical to wait_n except task_wait_random is
    being called.
    """
    items = []

    for _ in range(n):
        items.append(task_wait_random(max_delay))

    return [await item for item in asyncio.as_completed(items)]
