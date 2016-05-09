#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 Module"""

import task_01


def fibo(count):
    """Defines a function to build a list

        Args:
            count (int): Number of integers to return in the sequence.

            Returns:
        list: A list of Fibonacci numbers.

        Exmaples:
            >>> fibo(5)
            {0, 1, 1, 2, 3]
    """

    return [val for val in task_01.xfibo(count)]
