#!/usr/bin/python3
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
    while temp != 1:
        if (temp % div == 0):
            temp = temp/div
            sum += div
        else:
            div += 1
    if n == sum:
        return sum + 1
    return sum
