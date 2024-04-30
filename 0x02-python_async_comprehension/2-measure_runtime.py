#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
import time
from typing import List


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure the total runtime and return it"""
    start_time: float = time.time()
    list_task: List = []
    for _ in range(4):
        list_task.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(* list_task)
    return time.time() - start_time
