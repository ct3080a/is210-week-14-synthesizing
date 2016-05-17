#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring for a Fibonacci function"""


def xfibo(count):
    """A docstring for a Fibonacci sequence.

    Args:
        count (int): Number is amount of Fibonacci numbers generated.

    Returns:
        int: A sequence of integers generated in a Fibonacci sequence.

    Examples:

        >>> for i in xfibo(5):
        ...     print i
        0
        1
        1
        2
        3
    """
    fibprev = 0
    fibnext = 1
    fibcount = 0

    while fibcount < count:
        yield fibprev
        fibcount += 1
        fibprev, fibnext = fibnext, fibprev + fibnext
