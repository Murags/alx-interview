def pascal_triangle(n):
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
    if n == 0:
        return 1

    return n * factorial(n -1)
