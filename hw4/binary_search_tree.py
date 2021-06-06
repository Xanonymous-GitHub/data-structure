from typing import Optional

try:
    from .tree_node import Node
except ImportError:
    from tree_node import Node


# auto-balanced-binary-search-tree (AVL tree) implemented by Xanonymous.
# worst case: O(log n)

class AVLTree:
    def __init__(self):
        self.__root: Optional[Node] = None

    def __str__(self):
        if self.__root is not None:
            self.__root.display()
        return str()

    __repr__ = __str__

    @staticmethod
    def __height(target: Optional[Node]) -> int:
        return -1 if target is None else target.height

    @staticmethod
    def __re_height(target: Optional[Node]) -> None:
        if target is not None:
            target.height = max(
                AVLTree.__height(target.left),
                AVLTree.__height(target.right),
            ) + 1

    def __set_balances(self, *nodes: Node) -> None:
        for node in nodes:
            self.__re_height(node)
            node.balance = self.__height(node.right) - self.__height(node.left)

    def __rotate_left(self, a: Node) -> Node:
        b = a.right
        b.parent = a.parent
        a.right = b.left

        if a.right is not None:
            a.right.parent = a

        b.left = a
        a.parent = b

        if b.parent is not None:
            if b.parent.right == a:
                b.parent.right = b
            else:
                b.parent.left = b

        self.__set_balances(a, b)
        return b

    def __rotate_right(self, a: Node) -> Node:
        b = a.left
        b.parent = a.parent
        a.left = b.right

        if a.left is not None:
            a.left.parent = a

        b.right = a
        a.parent = b

        if b.parent is not None:
            if b.parent.right != a:
                b.parent.left = b
            else:
                b.parent.right = b

        self.__set_balances(a, b)
        return b

    # LR
    def __rotate_left_then_right(self, target: Node) -> Node:
        target.left = self.__rotate_left(target.left)
        return self.__rotate_right(target)

    # RL
    def __rotate_right_then_left(self, target: Node) -> Node:
        target.right = self.__rotate_right(target.right)
        return self.__rotate_left(target)

    def __re_balance(self, target: Node) -> None:
        self.__set_balances(target)

        if target.balance == -2:
            if self.__height(target.left.left) >= self.__height(target.left.right):
                target = self.__rotate_right(target)
            else:
                target = self.__rotate_left_then_right(target)
        elif target.balance == 2:
            if self.__height(target.right.right) >= self.__height(target.right.left):
                target = self.__rotate_left(target)
            else:
                target = self.__rotate_right_then_left(target)

        if target.parent is not None:
            self.__re_balance(target.parent)
        else:
            self.__root = target

    def __delete(self, node: Node) -> None:
        if node.left is None and node.right is None:
            if node.parent is None:
                # if tree has only root node.
                self.__root = None
            else:
                parent = node.parent

                # disconnect node and its parent.
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None

                self.__re_balance(parent)
            return

        if node.left is not None:
            # child is the root of the left sub-tree of node.
            child = node.left

            # find the node which has the biggest key in the sub-tree.
            while child.right is not None:
                child = child.right

        else:
            # child is the root of the right sub-tree of node.
            child = node.right

            # find the node which has the smallest key in the sub-tree.
            while child.left is not None:
                child = child.left

        # copy the child's key of the sub-tree to the deleted place.
        node.key = child.key

        # remove the child whose value has already been copied to another place.
        self.__delete(child)

    def __search(self, root: Optional[Node], key: int) -> Optional[Node]:
        if root is None or root.key == key:
            return root

        if root.key > key:
            return self.__search(root.left, key)

        return self.__search(root.right, key)

    def __print_property(self, root: Optional[Node]) -> None:
        if root is not None:
            self.__print_property(root.left)
            print('Node {0}, HEIGHT={1}, BF={2}'.format(root.key, root.height, root.balance))
            self.__print_property(root.right)

    def insert(self, key: int) -> bool:
        if self.__root is None:
            self.__root = Node(key)
            return True

        current = self.__root

        while True:
            if current.key == key:
                # node has same key does not allowed in BTS.
                return False

            parent = current

            # happened when the new key is smaller than the root of a sub-tree.
            should_go_left = current.key > key

            if should_go_left:
                current = current.left
            else:
                current = current.right

            if current is None:
                new_node = Node(key, parent)

                if should_go_left:
                    parent.left = new_node
                else:
                    parent.right = new_node

                self.__re_balance(parent)
                break

        return True

    def delete(self, key_to_delete: int) -> None:
        if self.__root is None:
            # tree is empty.
            return

        target = self.__root

        while target is not None:
            if key_to_delete > target.key:
                target = target.right
            elif key_to_delete < target.key:
                target = target.left
            else:
                self.__delete(target)
                return

    def search_key(self, key: int) -> str:
        result = self.__search(self.__root, key)
        return 'Not found.\n' if result is None else '{} is found.\n'.format(key)

    def print_property(self) -> None:
        self.__print_property(self.__root)

    def __preorder_traversal(self, root: Optional[Node] = None) -> None:
        if root is not None:
            print(root.key, end=' ')
            self.__preorder_traversal(root.left)
            self.__preorder_traversal(root.right)

    def preorder_traversal(self) -> None:
        print('preorder_traversal')
        self.__preorder_traversal(self.__root)
        print()

    def __inorder_traversal(self, root: Optional[Node] = None) -> None:
        if root is not None:
            self.__inorder_traversal(root.left)
            print(root.key, end=' ')
            self.__inorder_traversal(root.right)

    def inorder_traversal(self) -> None:
        print('inorder_traversal')
        self.__inorder_traversal(self.__root)
        print()

    def __postorder_traversal(self, root: Optional[Node] = None) -> None:
        if root is not None:
            self.__postorder_traversal(root.left)
            self.__postorder_traversal(root.right)
            print(root.key, end=' ')

    def postorder_traversal(self) -> None:
        print('postorder_traversal')
        self.__postorder_traversal(self.__root)
        print()


BinarySearchTree = AVLTree
