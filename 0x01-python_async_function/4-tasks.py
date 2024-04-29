#!/usr/bin/env python3
"""4. Tasks"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ spawn wait_random n times with the specified max_delay"""
    list_task: List = []
    for _ in range(n):
        task = task_wait_random(max_delay)
        list_task.append(task)
    delays = await asyncio.gather(* list_task)
    return sorted(delays)
