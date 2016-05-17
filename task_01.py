#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01 Module"""


def xfibo(count):
    """Defines a function for a Fibonacci generator

    Args:
        count (int): Number of integers to return in the sequence.

    Returns:
        list: A list of Fibonacci numbers.

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
    while iteration < count:
        yield lastnum
        iteration += 1
        lastnum, curnum = curnum, lastnum + curnum
