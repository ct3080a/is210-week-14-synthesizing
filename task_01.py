#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01."""


def xfibo(count):
    """A fibonacci function.

    Args:
        count (int): The number of Fibonacci numbers to return.

    Returns:
        int: The number in 'count'.

    Examples:
        >>> for i in xfibo(5):
                print i
        0
        1
        1
        2
        3
    """
    iteration = 0
    lastnum, curnum = 0, 1
    numbers = lastnum
    while iteration < count:
        yield numbers
        numbers = curnum
        lastnum, curnum = curnum, lastnum + curnum
        iteration += 1
