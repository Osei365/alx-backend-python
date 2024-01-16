#!/usr/bin/env python3
'''module for concurrent coroutines.'''

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''concurrent coroutine'''
    task_list = [task_wait_random(max_delay) for i in range(n)]
    result = await asyncio.gather(*task_list)
    return sorted(result)
