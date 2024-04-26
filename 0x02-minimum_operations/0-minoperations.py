#!/usr/bin/env python3
"""
finding the minimum operation needed
"""


def minOperations(n: int) -> int:
    """
    function that returns
    the minimum operations needed
    """
    temp: int = n
    div: int = 2
    sum: int = 0
    if n == 0:
        return 0
    for i in range(div, n):
        if temp == 1:
            break
        if (div % n == 0):
            temp = temp/div
            sum += div
        else:
            div += 1
    return sum
