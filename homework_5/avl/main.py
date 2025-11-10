from typing import Any


class Node:
    def __init__(self, key: Any):
        self.key = key
        self.left: Node = None
        self.right: Node = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root: Node = None

    def height(self, node: Node) -> int:
        if not node:
            return 0
        return node.height

    def balance_factor(self, node: Node) -> int:
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node: Node) -> None:
        if not node:
            return
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def rotate_right(self, y):
        """
        Правый поворот вокруг узла y.

             y                x
            / \              / \
           x   C    =>      A   y
          / \                  / \
         A   B                B   C
        """
        x = y.left
        B = x.right

        x.right = y
        y.left = B

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        """
        Левый поворот вокруг узла x.

           x                  y
          / \                / \
         A   y      =>      x   C
            / \            / \
           B   C          A   B
        """
        y = x.right
        B = y.left

        y.left = x
        x.right = B

        self.update_height(x)
        self.update_height(y)

        return y

    def insert(self, key: Any) -> None:
        self.root = self._insert(self.root, key)

    def _insert(self, node: Node, key: Any) -> Node:
        if not node:
            return Node(key)

        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node

        self.update_height(node)
        balance = self.balance_factor(node)

        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        return node

    def delete(self, key: Any) -> None:
        self.root = self._delete(self.root, key)

    def _delete(self, node: Node, key: Any) -> Node:
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        if not node:
            return node

        self.update_height(node)
        balance = self.balance_factor(node)

        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.rotate_right(node)

        if balance > 1 and self.balance_factor(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.rotate_left(node)

        if balance < -1 and self.balance_factor(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def _min_value_node(self, node: Node) -> Node:
        current = node
        while current.left:
            current = current.left
        return current

    def search(self, key: Any) -> bool:
        return self._search(self.root, key)

    def _search(self, node: Node, key: Any) -> bool:
        if not node or node.key == key:
            return node is not None

        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def inorder(self) -> list[Any]:
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node: Node, result: list[Any]) -> None:
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)

    def is_balanced(self) -> bool:
        return self._is_balanced(self.root)

    def _is_balanced(self, node: Node) -> bool:
        if not node:
            return True

        balance = self.balance_factor(node)
        if abs(balance) > 1:
            return False

        return self._is_balanced(node.left) and self._is_balanced(node.right)

    def get_height(self):
        return self.height(self.root)
