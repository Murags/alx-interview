#!/usr/bin/python3

def island_perimeter(grid):
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += check_up(grid, i, j)
                perimeter += check_right(grid, i, j)
                perimeter += check_down(grid, i, j)
                perimeter += check_left(grid, i, j)

    return perimeter


def check_up(grid, i, j):
    if i == 0:
        return 0

    if grid[i - 1][j] == 0:
        return 1

    return 0


def check_right(grid, i, j):
    if j == len(grid[i]) - 1:
        return 0

    if grid[i][j + 1] == 0:
        return 1

    return 0


def check_down(grid, i, j):
    if i == len(grid) - 1:
        return 0

    if grid[i + 1][j] == 0:
        return 1

    return 0


def check_left(grid, i, j):
    if j == 0:
        return 0

    if grid[i][j - 1] == 0:
        return 1

    return 0
