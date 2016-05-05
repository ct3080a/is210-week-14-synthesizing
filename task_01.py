#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module reates a new Fibonacci Generator."""


def xfibo(count):
    """This functions iterates the value of count.

    Agrs:
        count (Integer)

    Returns:
        yield each number in a Fibonacci sequence starting with 0.

    Examples:
    >>>
    """
    iteration = 0
    lastnum, curnum = 0, 1

    while iteration < count:
        yield lastnum
        iterations += 1
        lastnum, curnum = curnum, lastnum + curnum

