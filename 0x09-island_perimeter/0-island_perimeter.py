#!/usr/bin/python3
"""
mock interview question
"""


def island_perimeter(grid):
    """
    function that returns the perimeter
    of the grid
    """
    height = len(grid)
    for h in grid:
        width = len(h)
        break
    return height + width
