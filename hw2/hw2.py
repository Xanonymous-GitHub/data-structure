import sys

sys.setrecursionlimit(10 ** 6)


def recursive_addition(m: int, n: int) -> int:
    # Zero multiplied by any number is zero.
    if m == 0 or n == 0:
        return 0

    # In order to reduce the number of calculations, choose a smaller number as the multiplier.
    if m < n:
        m, n = n, m

    # Return the multiplicand, and the calculation result of the (multiplier - 1).
    return m + recursive_addition(m, n - 1)


def run():
    print(recursive_addition(2, 5) == 10)
    print(recursive_addition(3114, 3114) == 9696996)
    print(recursive_addition(5, 2) == 10)
    print(recursive_addition(0, 5) == 0)
    print(recursive_addition(2, 5) == 10)
    print(recursive_addition(8, 9) != 10)
