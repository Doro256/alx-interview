#!/usr/bin/python3
""" Script that prints Pascal's triangle """


def pascal_triangle(n):
    """ Function that returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []

    result = [[] for row in range(n)]

    for row in range(n):
        for col in range(row + 1):
            if (col < row):
                if (col == 0):
                    result[row].append(1)
                else:
                    result[row].append(
                        result[row - 1][col] + result[row - 1][col - 1])
            elif (col == row):
                result[row].append(1)
    return result
