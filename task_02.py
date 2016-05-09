#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A small docstring that generates a Fibnoacci list"""

import task_01


def fibo(count):
    """A docstring for a function that makes a Fibonacci list.

    Args:
        count (int): Number is amount of Fibonacci numbers generated.

    Returns:
        list: Fibonacci sequence of integers wrapped in a list by comprehension.

    Examples:

        >>> fibo(5)
        [0, 1, 1, 2, 3]
    """
    return [fibnumber for fibnumber in task_01.xfibo(count)]
