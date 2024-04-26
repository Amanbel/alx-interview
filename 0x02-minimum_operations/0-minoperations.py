#!/usr/bin/python3
"""
finding the minimum operation needed
"""


def minOperations(n):
    """
    function that returns
    the minimum operations needed
    """
    temp = n
    div = 2
    sum = 0
    if n < div:
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
