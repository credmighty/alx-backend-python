#!/usr/bin/env python3
"""Async basic"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    async coroutine that takes int arg
    waits for a random delay between 0 and max_delay and returns it.
    """
    rand_num = random.random() * max_delay
    await asyncio.sleep(rand_num)
    return rand_num
