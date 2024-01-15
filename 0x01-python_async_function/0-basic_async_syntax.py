#!/usr/bin/env python3
'''basic async task module'''


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''creates a corountine'''
    r = random.uniform(0, max_delay)
    await asyncio.sleep(r)
    return r
