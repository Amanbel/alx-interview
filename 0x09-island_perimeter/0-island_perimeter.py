#!/usr/bin/python3
"""
mock interview question
"""


def island_perimeter(grid):
    """
    function that returns the perimeter
    of the grid
    """
    height = 0
    width = 0
    max = 0
    for h in grid:
        if 1 in h:
            height += 1
    for h in grid:
        width = 0
        for w in h:
            if w == 1:
                width += 1
        if width > max:
            max = width
    return 2 * (max + height)
