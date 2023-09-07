#!/usr/bin/python3
""" Prime Game Problem
    Topic: Prime Checking
"""


def is_prime(n):
    """checks if number isa prime number"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def isWinner(x, nums):
    """
    Determines the winner in the prime game
    """
    Ben = 0
    Maria = 0

    for round in range(x):
        pr_count = sum(1 for num in range(2, nums[round] + 1) if is_prime(num))

        if pr_count % 2 == 0:
            Ben += 1
        else:
            Maria += 1

    if Ben == Maria:
        return None
    return 'Ben' if Ben > Maria else 'Maria'
