#!/usr/bin/python3
"""This module rotates a 2d matrix"""


def rotate_2d_matrix(matrix):
    """_summary_

    Args:
        matrix (_type_): _description_
    """
    matrix.reverse()
    mat_len = len(matrix)

    for i in range(mat_len):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
