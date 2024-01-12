#!/usr/bin/env python3
'''module that returns mixed tuples
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''gets key values in tuples
    '''
    return (k, float(v**2))
