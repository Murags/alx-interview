#!/usr/bin/python3
"""finds minimum coins for change"""


def makeChange(coins, total):
    """_summary_

    Args:
        coins (_type_): _description_
        total (_type_): _description_

    Returns:
        _type_: _description_
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    i = 0
    counter = 0

    for i in range(len(coins)):
        while (total >= coins[i]):
            total -= coins[i]
            counter += 1

    if total != 0:
        return -1

    return counter
