#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02."""

import task_01


def fibo(count):
    """Creates list using xfibo generator.

    Args:
        count (int): The total number of Fibonacci numbers to return.

    Returns:
        list: Number of Fibonacci sequences numbers by count variable.

    Examples:
        >>> fibo(5)
        [0, 1, 1, 2, 3]

        >>> fibo(7)
        [0, 1, 1, 2, 3, 5, 8]
    """
    numbers = [i for i in task_01.xfibo(count)]
    return numbers
