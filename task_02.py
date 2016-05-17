#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""Task 2 docstring."""


import task_01


def fibo(count):
    """Function that returns the Fibonnaci numbers.

    Args:
        count(int): The total numberr of FIbonacci numbers to return.

    Return:
        num in task_01.xfibo()(list): A list comprehension that uses
                                      task_01.xfibo().

    Examples:

        >>> fibo(5)
        [0, 1, 1, 2, 3]
    """
    return [num for num in task_01.xfibo(count)]
