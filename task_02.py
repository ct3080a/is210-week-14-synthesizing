#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""I felt like crashing my machine this time."""

import task_01


def fibo(count):
    """Takes task_01.xfibo and turns it into a list

    Args:
        count(int): how many numbers will be spit out
    Returns:
        fibonacci sequence until count numbers spit out

    Examples:
        >>> fibo(5)
        [0, 1, 1, 2, 3]
    """
    nyoom = [num for num in task_01.xfibo(count)]
    return nyoom
