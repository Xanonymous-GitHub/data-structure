import sys

from .binary_search_tree import BinarySearchTree

sys.setrecursionlimit(1000000)


def run():
    tree = BinarySearchTree()

    test_max_key = 39

    for x in range(1, test_max_key + 1):
        tree.insert(x)

    print('BinarySearchTree which has {} nodes\n'.format(test_max_key))
    print(tree)

    tree.preorder_traversal()
    print()

    tree.inorder_traversal()
    print()

    tree.postorder_traversal()
    print()

    for x in range(1, test_max_key + 1):
        tree.delete(x)
