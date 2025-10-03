from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self._top = None
        self.size = 0

    def is_empty(self) -> bool:
        return self._top is None

    def push(self, data: Any):
        new_node = Node(data)
        new_node.next = self._top
        self._top = new_node
        self.size += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Pop from empty stack")

        data = self._top.data
        self._top = self._top.next
        self.size -= 1
        return data

    def top(self) -> Any:
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._top.data

    def __len__(self) -> int:
        return self.size
