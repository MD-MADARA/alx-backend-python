#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start_time = time.time()
    list_task = []
    for _ in range(4):
        list_task.append(asyncio.create_task(async_comprehension()))
    await asyncio.gather(* list_task)
    return time.time() - start_time
