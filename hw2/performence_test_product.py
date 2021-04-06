import sys
import timeit as ti

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


execution_data: [tuple[tuple[int, int]]] = (
    ((69, 0), (491, 86), (27, 134), (85, 69), (4, 99)),
    ((0, 9487), (99, 47), (423, 19), (5, 2), (311, 13)),
    ((251, 79), (957, 60), (55, 8), (60, 54), (811, 40)),
    ((954, 74), (54, 23), (478, 45), (12, 2), (31, 3)),
    ((9, 987), (29, 41), (323, 59), (4, 88), (111, 11))
)


def recursive_test(test_number: int):
    [recursive_multiplication(*execution_data[test_number][k % 5]) for k in range(100)]


def iterative_test(test_number: int):
    [iterative_multiplication(*execution_data[test_number][k % 5]) for k in range(100)]


def rec_and_iter_test():
    print()
    print("Running time comparison:")
    print()

    t_rec_total = 0
    t_ite_total = 0

    for c in range(5):

        t_start = ti.default_timer()
        for i in range(10000):
            recursive_test(c)
        tend = ti.default_timer()
        t_rec = tend - t_start

        t_start = ti.default_timer()
        for i in range(10000):
            iterative_test(c)
        tend = ti.default_timer()
        t_ite = tend - t_start

        print()
        print("Recursive approach test {0}:".format(c + 1), t_rec)
        t_rec_total += t_rec
        print("iterative approach test {0}:".format(c + 1), t_ite)
        t_ite_total += t_ite
        print()
    print('total rec time:', t_rec_total)
    print('total ite time:', t_ite_total)
    print('total time:', t_ite_total + t_rec_total)

    print()
    print("Running time comparison (Timer Method 2):")
    print()

    t_rec_total = 0
    t_ite_total = 0

    for x in range(5):
        t_rec = ti.timeit("recursive_test({0})".format(x), setup="from __main__ import recursive_test", number=10000)
        t_ite = ti.timeit("iterative_test({0})".format(x), setup="from __main__ import iterative_test", number=10000)

        print()
        print("Recursive approach test {0}:".format(x + 1), t_rec)
        t_rec_total += t_rec
        print("iterative approach test {0}:".format(x + 1), t_ite)
        t_ite_total += t_ite
        print()
    print('total rec time:', t_rec_total)
    print('total ite time:', t_ite_total)
    print('total time:', t_ite_total + t_rec_total)


def main():
    rec_and_iter_test()


if __name__ == '__main__':
    main()
