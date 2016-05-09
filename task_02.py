#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02"""


import task_01


def fibo(count):
    """Return a list of Fibonacci numbers. count(int):
    the total number of Fibonacci numbers"""

    return [num for num in task_01.xfibo(count)]
