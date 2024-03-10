#!/usr/bin/python3

def pascal_triangle(n):
    if n <= 0:
        return []
    triangle = []
    row = []
    for i in range(0, n):
        row = []
        for j in range(0, i + 1):
            if j == 0:
                row.append(1)
            else:
                if len(triangle[i - 1]) > j:
                    el = triangle[i - 1][j] + triangle[i - 1][j - 1]
                    row.append(el)
                else:
                    row.append(1);
        triangle.append(row)
    return triangle
