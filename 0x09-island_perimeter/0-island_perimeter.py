#!/usr/bin/python3

def island_perimeter(grid):
    """ Function that that returns the perimeter of the
        island described in grid
    """
    # Initialize perimeter and dimensions of the grid
    perimeter = 0
    n = len(grid)
    m = len(grid[0])

    # Traverse the grid to count the perimeter
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                # Count top edge
                if i == 0 or grid[i - 1][j] == 0:
                    perimeter += 1
                # Count bottom edge
                if i == n - 1 or grid[i + 1][j] == 0:
                    perimeter += 1
                # Count left edge
                if j == 0 or grid[i][j - 1] == 0:
                    perimeter += 1
                # Count right edge
                if j == m - 1 or grid[i][j + 1] == 0:
                    perimeter += 1

    return perimeter
