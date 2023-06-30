#!/usr/bin/python3
"""pascals triangle coefficients"""


def pascal_triangle(n):
    """Gets the coeffients and return list of list"""
    co_efficient_list = []

    if n <= 0:
        return co_efficient_list

    for x in range(n):
        row = []
        for i in range(x + 1):
            num = factorial(x)
            denom = factorial(i) * factorial(x - i)
            row.append(num // denom)

        co_efficient_list.append(row)

    return co_efficient_list


def factorial(n):
    """Gets factorial of a number"""
    if n == 0:
        return 1

    return n * factorial(n - 1)
