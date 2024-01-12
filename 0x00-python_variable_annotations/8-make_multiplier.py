#!/usr/bin/env python3
'''return callable
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates a callable
    '''
    return lambda x: x * multiplier
