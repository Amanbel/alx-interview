#!/usr/bin/python3
"""
interview question - find winner
"""


def isWinner(x, nums):
    """
    function that returns the winner
    """
    maria = 2
    mariasSet = []
    ben = 3
    j = 0
    bensSet = []
    while x > 0:
        for i in range(1, nums[j] + 1):
            if maria % i == 0:
                mariasSet.append(i)
        for i in range(1, nums[j] + 1):
            if ben % i == 0:
                bensSet.append(i)
        if nums[j] == 1:
            bensSet.append(1)
        maria += 1
        ben += 1
        x -= 1
        j += 1
    if len(bensSet) > len(mariasSet):
        return "Ben"
    elif len(bensSet) == len(mariasSet):
        return None
    else:
        return "Maria"
