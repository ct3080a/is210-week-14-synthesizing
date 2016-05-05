#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Fibonacci returns once again."""

import task_01


def fibo(count):
    """A Fibonacci sequence generator.

    Args:
        count (int): Number of Fibonacci numbers to return.

    Returns:
        list: Fibonacci sequence in a list comprehension.

    Examples:
        >>>
    """
    return [fibnumber for fibnumber in task_01.xfibo(count)]
