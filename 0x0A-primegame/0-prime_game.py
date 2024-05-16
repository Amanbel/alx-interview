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
    mariasPick = []
    ben = 3
    bensSet = []
    bensPick = []
    while x > 0:
        x -= 1
        for n in nums:
            for i in range(1, n + 1):
                if maria % i == 0:
                    mariasSet.append(i)
                    mariasPick.append(i)
            for i in range(1, n + 1):
                if ben in mariasPick:
                    ben += 1
                if ben % i == 0:
                    bensSet.append(i)
            if n == 1:
                bensSet.append(1)
            maria += 1
            ben += 1
    if len(bensSet) > len(mariasSet):
        return "Ben"
    elif len(bensSet) == len(mariasSet):
        return None
    else:
        return "Maria"
