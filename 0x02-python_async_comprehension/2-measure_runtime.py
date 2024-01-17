#!/usr/bin/env python3
'''measuring time of async comprehension function'''

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measures runtime for an async comprehension.'''
    s = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    elapsed = time.perf_counter() - s
    return elapsed
