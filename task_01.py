#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fibonacci returns."""


def xfibo(count):
    """A Fibonacci generator sequence.

    Args:
        count (int): Number of Fibonacci numbers to return.

    Returns:
        int: Sequence of integers.

    Examples:
        >>>
    """
    fibprev = 0
    fibnext = 1
    fibcount = 0

    while fibcount < count:
        yield fibprev
        fibcount += 1
        fibprev, fibnext = fibnext, fibprev + fibnext
