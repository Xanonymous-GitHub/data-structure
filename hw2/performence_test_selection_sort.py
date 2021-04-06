import timeit as ti
import random
import copy
import sys

sys.setrecursionlimit(10 ** 6)


def iterative_selection_sort(collection: [int or float]) -> [int or float]:
    length: int = len(collection)

    for v in range(length - 1):
        least: int = v

        for k in range(v + 1, length):
            if collection[k] < collection[least]:
                least = k

        if least != v:
            collection[least], collection[v] = (collection[v], collection[least])

    return collection


def recursive_selection_sort(collection: [int or float]) -> [int or float]:
    def find_min_index(_collection: [int or float], a: int, b: int) -> int:
        if a == b:
            return a

        k: int = find_min_index(_collection, a + 1, b)

        return a if _collection[a] < _collection[k] else k

    def recursive(_collection: [int or float], length: int, pos: int = 0):
        if pos == length:
            return -1

        v: int = find_min_index(_collection, pos, length - 1)

        if v != pos:
            _collection[pos], _collection[v] = (_collection[v], _collection[pos])

        recursive(_collection, length, pos + 1)

    recursive(collection, len(collection))
    return collection


unsorted = list()


def generate_random_list(size: int):
    unsorted.clear()
    for _ in range(size):
        random.seed()
        unsorted.append(random.randrange(-99999, 100000))
    return unsorted


print('Generating random unsorted lists... ', sep='', end='')

unsorted_sets = (
    generate_random_list(10000),
    generate_random_list(10000),
    generate_random_list(10000),
    generate_random_list(10000),
    generate_random_list(10000),
)

print('Done.')

# ---------------------------------------------------------Method 1
print()
print("Running time comparison (Timer Method 1):")
print()

t_rec_total = 0
t_ite_total = 0

for index, unsorted_list in enumerate(unsorted_sets):
    new_unsorted_list = copy.deepcopy(unsorted_list)
    t_start = ti.default_timer()
    recursive_selection_sort(new_unsorted_list)
    t_end = ti.default_timer()
    t_rec = t_end - t_start
    t_rec_total += t_rec

    new_unsorted_list = copy.deepcopy(unsorted_list)
    t_start = ti.default_timer()
    iterative_selection_sort(copy.deepcopy(new_unsorted_list))
    t_end = ti.default_timer()
    t_ite = t_end - t_start
    t_ite_total += t_ite

    print()
    print('The array of [RANDOM-SET-{0}] has been sorted.'.format(index + 1))
    print('Recursive approach:', t_rec)
    print('Iterative approach:', t_ite)
    print()

print('total rec time:', t_rec_total)
print('total ite time:', t_ite_total)
print('total time:', t_ite_total + t_rec_total)

# ---------------------------------------------------------Method 2
print()
print("Running time comparison (Timer Method 2):")
print()

for d in range(5):
    t_ite = ti.timeit("iterative_selection_sort(copy.deepcopy(unsorted_sets[{0}]))".format(d),
                      setup="from __main__ import iterative_selection_sort, unsorted_sets, copy", number=1)
    t_rec = ti.timeit("recursive_selection_sort(copy.deepcopy(unsorted_sets[{0}]))".format(d),
                      setup="from __main__ import recursive_selection_sort, unsorted_sets, copy", number=1)

    print()
    print('The array of [RANDOM-SET-{0}] has been sorted.'.format(d + 1))
    print('Recursive approach:', t_rec)
    print('Iterative approach:', t_ite)
    print()

print('total rec time:', t_rec_total)
print('total ite time:', t_ite_total)
print('total time:', t_ite_total + t_rec_total)
