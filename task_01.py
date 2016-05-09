#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 01"""


def xfibo(count):
    """Fibonacci sequence function. count (int): chosen number."""
    iterations = 0
    lastnum = 0
    curnum = 1
    while iterations < count:
        yield lastnum
        lastnum, curnum = curnum, curnum + lastnum
        iterations += 1
