#!/usr/bin/env python3
'''module for async func generator.'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    '''creates a an async generator.'''
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
