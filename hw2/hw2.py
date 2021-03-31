import sys

sys.setrecursionlimit(10 ** 6)


def recursive_multiplication(m: int, n: int) -> int:
    # Zero multiplied by any number is zero.
    if m == 0 or n == 0:
        return 0

    # In order to reduce the number of calculations, choose a smaller number as the multiplier.
    if m < n:
        m, n = n, m

    # Return the multiplicand, and the calculation result of the (multiplier - 1).
    return m + recursive_multiplication(m, n - 1)


def iterative_multiplication(m: int, n: int) -> int:
    # Zero multiplied by any number is zero.
    if m == 0 or n == 0:
        return 0

    # In order to reduce the number of calculations, choose a smaller number as the multiplier.
    if m < n:
        m, n = n, m

    result: int = 0
    for _ in range(n):
        result += m
    return result


def run():
    print(recursive_multiplication(2, 5) == 10)
    print(recursive_multiplication(3114, 3114) == 9696996)
    print(recursive_multiplication(5, 2) == 10)
    print(recursive_multiplication(0, 5) == 0)
    print(recursive_multiplication(2, 5) == 10)
    print(recursive_multiplication(8, 9) != 10)

    print(iterative_multiplication(2, 5) == 10)
    print(iterative_multiplication(3114, 3114) == 9696996)
    print(iterative_multiplication(5, 2) == 10)
    print(iterative_multiplication(0, 5) == 0)
    print(iterative_multiplication(2, 5) == 10)
    print(iterative_multiplication(8, 9) != 10)
