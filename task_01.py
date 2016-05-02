#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fib sequence"""


def xfibo(count):
    """Xfibo creates a list of Fibonacci numbers.
    Arguments:
        count(int): Number of Fib numbers
    Returns:
        Fib Sequence up until the number given
    Examples:
        >>>for i in xfibo(7)
            print i
            0
            1
            1
            2
            3
            5
            8
    """
    counter = 0
    prenum, num = 0, 1
    while counter < count:
        yield num
        prenum, num = num, num + prenum
        counter += 1
