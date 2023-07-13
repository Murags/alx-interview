#!/usr/bin/python3
"""
This script defines a function to calculate the minimum number of
operations required to transform a given number 'n' into 1.
The function utilizes a prime factorization
approach to calculate the operations.
"""


def minOperations(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations
