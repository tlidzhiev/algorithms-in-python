from typing import Any


class Node:
    def __init__(self, data: Any):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self._front = None
        self._back = None
        self.size = 0

    def is_empty(self) -> bool:
        return self._front is None

    def push(self, data: Any):
        new_node = Node(data)

        if self.is_empty():
            self._front = self._back = new_node
        else:
            self._back.next = new_node
            self._back = new_node

        self.size += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("Pop from empty queue")

        data = self._front.data
        self._front = self._front.next

        if self._front is None:
            self._back = None

        self.size -= 1
        return data

    def top(self) -> Any:
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self._front.data

    def __len__(self) -> int:
        return self.size
