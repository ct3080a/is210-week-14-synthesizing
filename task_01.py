#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module  reates a new Fibonacci Generator."""


def xfibo(count):
    """This functions iterates the value of count.
    Agrs:
        count (Integer)
    Returns:
        yield each number in a Fibonacci sequence starting with 0.
    Examples:
    >>> for num in xfibo(5):
	print num	
    0
    1
    2
    3
    4
    >>> for num in xfibo(2):
	print num	
    0
    1
    >>> for num in xfibo(3):
	print num	
    0
    1
    2
    """
    iterations = 0
    while iterations < count:
            yield iterations 
            iterations += 1
       

