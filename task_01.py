#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generator task for week 14 synthesizing"""


def xfibo(count):
    """Fibonacci sequence generator function.

    Args:
        count (int): Number of integers to return in the sequence.

    Yields:
        int: The next in the list of Fibonacci numbers.

    Examples:
        >>> xfibo(10)
        0
        1
        1
        2
        3
        5
        8
        13
        21
        34
    """
    iteration = 0
    lastnum, curnum = 0, 1

    while iteration < count:

        yield lastnum
        lastnum, curnum = curnum, lastnum + curnum
        iteration += 1
