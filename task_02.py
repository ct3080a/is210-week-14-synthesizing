#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Starter data module"""

import task_01


def fibo(count):
    """This functions uses a comprehension list to wrap a generator.
        Args:
            count(integer)
        Returns:
            list comprehension
        Examples:'
        >>> fibo(10)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        >>> fibo (15)
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        >>> fibo(5)
        [0, 1, 2, 3, 4]
    """
    [num for num in task_01.xfibo(count)]
