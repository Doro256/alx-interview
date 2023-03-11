#!/usr/bin/python3

import sys


def nqueens(n):
    """ N queens puzzle """

    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    if not n.isnumeric():
        print('N must be a number')
        sys.exit(1)

    n = int(n)
    if n < 4:
        print('N must be atleast 4')
        sys.exit(1)

chessboard = []

