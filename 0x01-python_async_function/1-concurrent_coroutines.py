#!/usr/bin/env python3
"""multiple coroutines at the same time with async"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ spawn wait_random n times with the specified max_delay"""
    list_task: List = []
    for _ in range(n):
        task = asyncio.create_task(wait_random(max_delay))
        list_task.append(task)
    delays = await asyncio.gather(* list_task)
    return sorted(delays)
