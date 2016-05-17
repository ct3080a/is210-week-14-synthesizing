#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""I felt like crashing my machine this time."""


def xfibo(count):
    """creates the fibonacci sequence

    Args:
        count(int): how many numbers xfibo will spit out
    Returns:
        fibonacci sequence until count numbers spit out

    Examples:
        >>>for i in xfibo(5)
            print i
            0
            1
            1
            2
            3
    """
    iteration = 0
    lastnum, curnum = 0, 1
    while iteration < count:
        yield lastnum
        lastnum, curnum = curnum, curnum + lastnum
        iteration += 1
