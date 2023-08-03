#!/usr/bin/python3

from sys import argv


def safe(board, col, row, n):
    """_summary_

    Args:
        board (_type_): _description_
        col (_type_): _description_
        row (_type_): _description_
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    # same column check
    for i in range(n):
        if board[i][col] == 1:
            return False
    i, j = row, col

    # left diagonal check
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row, col
    # right diagonal check
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def main():
    """_summary_
    """
    if len(argv) == 1:
        return
    n = argv[1]
    try:
        n = int(n)
    except Exception:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]

    def backtrack(row):
        """_summary_

        Args:
            row (_type_): _description_
        """
        if row == n:
            # prints the queen positions
            output = []
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        output.append([i, j])
            print(output)
            return

        for col in range(n):
            if safe(board, col, row, n):
                board[row][col] = 1
                backtrack(row + 1)
                board[row][col] = 0
    backtrack(0)


if __name__ == "__main__":
    main()
