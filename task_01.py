#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 1 docstring."""


def xfibo(count):
    """Fibonacci sequence generator.

    Args:
        count(int): The number of Fibonacci numbers to return.

    Yield:
        num_a(int): Number in a Fibonacci sequence starting with 0.

    Examples:

    >>> for i in xfibo(5):
             print i
    0
    1
    1
    2
    3
    """
    num = 0
    num_a, num_b = 0, 1
    while num < count:
        yield num_a
        num_a, num_b = num_b, num_a + num_b
        num += 1
