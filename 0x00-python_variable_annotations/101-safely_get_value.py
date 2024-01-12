#!/usr/bin/env python3
'''module for typevar.
'''
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    '''safely get values.
    '''
    if key in dct:
        return dct[key]
    else:
        return default
