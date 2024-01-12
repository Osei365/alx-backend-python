#!/usr/bin/env python3
'''module task 101.'''
from typing import Any, Mapping, Union, TypeVar


T = TypeVar('T')
tvar = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: tvar = None) -> Union[Any, tvar]:
    ''' safe get value.'''
    if key in dct:
        return dct[key]
    else:
        return default
