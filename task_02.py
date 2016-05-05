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
    """
    return [num for num in task_01.xfibo(count)]
