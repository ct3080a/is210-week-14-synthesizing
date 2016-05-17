#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A module with list comprehension that builds a list."""


import task_01


def fibo(count):
    """A list builder.
    Arguments:
        count(int): number of items that will be returned.
    Returns:
        list of fib numbers to number from input
    Examples:
        >>>fibo(6)
        [0, 1, 1, 2, 3, 5]
    """
    fibolist = [num for num in task_01.xfibo(count)]
    return fibolist
