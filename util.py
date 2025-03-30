# util.py
# Author: [Your Name]
# Date: April 21, 2024
# Utility functions for 4x4 grid manipulation.

def create_grid(grid):
    """
    Create a 4x4 grid filled with zeroes and assign it to the given list.
    :param grid: An empty list that will be filled with a 4x4 grid.
    """
    # Clear existing content in the grid (if any)
    grid.clear()
    # Create a 4x4 grid filled with zeroes
    for _ in range(4):
        grid.append([0, 0, 0, 0])


def print_grid(grid):
    """
    Print a 4x4 grid in 5-width columns within a box.
    :param grid: A 4x4 grid (list of lists).
    """
    # Top border
    print("+" + "-" * 20 + "+")
    # Print each row with formatted spacing
    for row in grid:
        line = "|"
        for item in row:
            # Print a 5-space wide item
            line += f"{item if item != 0 else '':>5}"
        line += "|"
        print(line)
    # Bottom border
    print("+" + "-" * 20 + "+")


def check_lost(grid):
    """
    Check if the game is lost. The game is lost if there are no zeroes
    and no adjacent equal values.
    :param grid: A 4x4 grid (list of lists).
    :return: True if the game is lost, otherwise False.
    """
    # Check for zeroes
    for row in grid:
        if 0 in row:
            return False  # If there's a zero, the game is not lost
    
    # Check for adjacent equal values (horizontally and vertically)
    for i in range(4):
        for j in range(4):
            if (j < 3 and grid[i][j] == grid[i][j + 1]) or (i < 3 and grid[i][j] == grid[i + 1][j]):
                return False  # If adjacent values are equal, the game is not lost
    
    return True  # If no zeroes and no adjacent equal values, the game is lost


def check_won(grid):
    """
    Check if the game is won. The game is won if a value >= 32 is found in the grid.
    :param grid: A 4x4 grid (list of lists).
    :return: True if a value >= 32 is found, otherwise False.
    """
    for row in grid:
        if any(item >= 32 for item in row):
            return True  # If a value >= 32 is found, the game is won
    return False  # Otherwise, the game is not won


def copy_grid(grid):
    """
    Create a copy of the given 4x4 grid.
    :param grid: A 4x4 grid (list of lists).
    :return: A new 4x4 grid that is a copy of the input grid.
    """
    # Copy each row to create a new grid
    return [row.copy() for row in grid]


def grid_equal(grid1, grid2):
    """
    Check if two 4x4 grids are equal.
    :param grid1: The first grid.
    :param grid2: The second grid.
    :return: True if the grids are equal, otherwise False.
    """
    for i in range(4):
        if grid1[i] != grid2[i]:  # If any row differs, the grids are not equal
            return False
    return True  # If all rows are identical, the grids are equal