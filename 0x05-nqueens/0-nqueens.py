#!/usr/bin/python3

import sys


def solve_n_queens(n):
    # Initialize the chessboard as an empty n x n matrix
    chessboard = [[0] * n for _ in range(n)]

    # Define a function to check if a queen can be placed at a given row and
    # column
    def is_safe(row, col):
        # Check the row
        for i in range(col):
            if chessboard[row][i] == 1:
                return False

        # Check the upper diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if chessboard[i][j] == 1:
                return False

        # Check the lower diagonal
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if chessboard[i][j] == 1:
                return False

        return True

    # Define a recursive function to place queens on the chessboard
    def place_queen(col):
        # Base case: all queens have been placed
        if col == n:
            # Print the solution
            for row in range(n):
                print([row, chessboard[row].index(1)])
            print()
            return

        # Try placing a queen in each row of the current column
        for row in range(n):
            if is_safe(row, col):
                # Place the queen
                chessboard[row][col] = 1

                # Recursively place the remaining queens
                place_queen(col + 1)

                # Remove the queen (backtrack)
                chessboard[row][col] = 0

    # Start placing queens in the first column
    place_queen(0)


# Parse the command-line argument
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)
try:
    n = int(sys.argv[1])
except ValueError:
    print("N must be a number")
    sys.exit(1)
if n < 4:
    print("N must be at least 4")
    sys.exit(1)

# Solve the N queens problem
solve_n_queens(n)
