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


class AutoIncreasingInteger(int):
    def __init__(self, value: int = 0):
        super().__init__()
        self.value = value

    def __repr__(self) -> int:
        current = self.value
        self.value += 1
        return current

    def __str__(self):
        return str(self.__repr__())


def rec_and_iter_test():
    executions = [recursive_multiplication, iterative_multiplication]
    execution_index: AutoIncreasingInteger = AutoIncreasingInteger(0)
    execution_data: [tuple[tuple[int, int]]] = (
        ((69, 0), (491, 86), (27, 134), (85, 69), (4, 99)),
        ((0, 9487), (99, 47), (423, 19), (5, 2), (311, 13)),
        ((251, 79), (957, 60), (55, 8), (60, 54), (811, 40)),
        ((954, 74), (54, 23), (478, 45), (12, 2), (31, 3)),
        ((9, 987), (29, 41), (323, 59), (4, 88), (111, 11))
    )

    def function(test_number: int):
        [executions[execution_index](*execution_data[test_number][k % 5]) for k in range(100)]

    # ---------------------------------------------------------Method 1
    print()
    print("Running time comparison:")
    print()

    t_rec_total = 0
    t_ite_total = 0

    for c in range(5):

        t_start = ti.default_timer()
        for i in range(10000):
            function(c)
        tend = ti.default_timer()
        t_rec = tend - t_start

        t_start = ti.default_timer()
        for i in range(10000):
            function(c)
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

    a = AutoIncreasingInteger()
    print(a)
    print(a)

    rec_and_iter_test()
