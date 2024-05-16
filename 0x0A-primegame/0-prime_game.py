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
            while len(mariasPick + bensPick) + 1 != n:
                for i in range(1, n + 1):
                    if i in bensPick:
                        continue
                    if maria % i == 0:
                        mariasSet.append(i)
                        mariasPick.append(i)
                for i in range(1, n + 1):
                    if i in mariasPick:
                        continue
                    if ben % i == 0:
                        bensSet.append(i)
                        bensPick.append(i)
                if n == 1:
                    bensSet.append(1)
                maria += 1
                ben += 1
            mariasPick = []
            bensPick = []
            maria = 2
            ben = 3
    if len(bensSet) > len(mariasSet):
        return "Ben"
    elif len(bensSet) == len(mariasSet):
        return None
    else:
        return "Maria"
