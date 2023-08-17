#!/usr/bin/env python3
"""This module rotates a 2d matrix"""


def rotate_2d_matrix(matrix):
    """_summary_

    Args:
        matrix (_type_): _description_
    """
    n = len(matrix[0])
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            print(matrix[n - 1 - j][i])
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
