from __future__ import annotations

from typing import Optional


class Node:
    def __init__(self, key: int = None, parent: Optional[Node] = None):
        self.__key = key
        self.__right = None
        self.__left = None
        self.__parent = parent
        self.__height = 0
        self.__balance = 0

    @property
    def key(self) -> int:
        return self.__key

    @key.setter
    def key(self, key: int) -> None:
        self.__key = key

    @property
    def right(self) -> Optional[Node]:
        return self.__right

    @right.setter
    def right(self, right: Optional[Node]) -> None:
        self.__right = right

    @property
    def left(self) -> Optional[Node]:
        return self.__left

    @left.setter
    def left(self, left: Optional[Node]) -> None:
        self.__left = left

    @property
    def parent(self) -> Optional[Node]:
        return self.__parent

    @parent.setter
    def parent(self, parent: Optional[Node]) -> None:
        self.__parent = parent

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int) -> None:
        self.__height = height

    @property
    def balance(self) -> int:
        return self.__balance

    @balance.setter
    def balance(self, balance: int) -> None:
        self.__balance = balance

    def __display_aux(self):
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left.__display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right.__display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left.__display_aux()
        right, m, q, y = self.right.__display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def display(self):
        lines, *_ = self.__display_aux()
        for line in lines:
            print(line)
