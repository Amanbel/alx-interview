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
    bensSet = []
    while x > 0:
        x -= 1
        for n in nums:
            maria += 1
            ben += 1
            for i in range(1, n + 1):
                if maria % i == 0:
                    mariasSet.append(i)
            for i in range(1, n + 1):
                if ben % i == 0:
                    bensSet.append(i)
    if len(bensSet) > len(mariasSet):
        return "Ben"
    elif len(bensSet) == len(mariasSet):
        return None
    else:
        return "Maria"