#!/usr/bin/env python3
'''module that handles iterable.'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' returns a list of tuples.'''
    return [(i, len(i)) for i in lst]
