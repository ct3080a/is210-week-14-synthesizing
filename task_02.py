#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""week 14 syntehsizing task to utilize the generator"""

from task_01 import xfibo


def fibo(count):
    """Fibonacci sequence generator function.

    Args:
        count (int): Number of integers to return in the sequence.

    Yields:
        list: The list of Fibonacci numbers.

    Examples:
        >>> fibo(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    """
    return [num for num in xfibo(count)]
