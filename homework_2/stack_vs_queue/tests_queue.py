from queue import Queue

import pytest


def test_queue_creation():
    queue = Queue()
    assert queue.is_empty()
    assert len(queue) == 0


@pytest.mark.parametrize(
    "elements, expected_size, expected_front",
    [
        ([1], 1, 1),
        ([1, 2], 2, 1),
        ([1, 2, 3], 3, 1),
        ([5, 10, 15, 20], 4, 5),
        (["a", "b", "c"], 3, "a"),
    ],
)
def test_push_elements(elements, expected_size, expected_front):
    queue = Queue()
    for elem in elements:
        queue.push(elem)
    assert not queue.is_empty()
    assert len(queue) == expected_size
    assert queue.top() == expected_front


@pytest.mark.parametrize(
    "elements, expected_order",
    [
        ([1, 2, 3], [1, 2, 3]),
        ([5, 10, 15], [5, 10, 15]),
        (["x", "y", "z"], ["x", "y", "z"]),
        ([42], [42]),
    ],
)
def test_pop_elements(elements, expected_order):
    queue = Queue()
    for elem in elements:
        queue.push(elem)

    result = []
    while not queue.is_empty():
        result.append(queue.pop())

    assert result == expected_order
    assert queue.is_empty()
    assert len(queue) == 0


@pytest.mark.parametrize(
    "operation, error_message",
    [
        ("pop", "Pop from empty queue"),
        ("top", "Peek from empty queue"),
    ],
)
def test_empty_queue_operations(operation, error_message):
    queue = Queue()
    with pytest.raises(IndexError, match=error_message):
        getattr(queue, operation)()


def test_top_does_not_remove_element():
    queue = Queue()
    queue.push(10)
    queue.push(20)

    assert queue.top() == 10
    assert len(queue) == 2
    assert queue.top() == 10
    assert len(queue) == 2


def test_fifo_behavior():
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)

    assert queue.pop() == 1
    assert queue.pop() == 2
    assert queue.pop() == 3


def test_alternating_operations():
    queue = Queue()

    queue.push(1)
    assert queue.pop() == 1

    queue.push(2)
    queue.push(3)
    assert queue.pop() == 2

    queue.push(4)
    assert queue.pop() == 3
    assert queue.pop() == 4


def test_size_tracking():
    queue = Queue()

    assert len(queue) == 0

    queue.push(1)
    assert len(queue) == 1

    queue.push(2)
    queue.push(3)
    assert len(queue) == 3

    queue.pop()
    assert len(queue) == 2

    queue.pop()
    queue.pop()
    assert len(queue) == 0


def test_large_number_of_elements():
    queue = Queue()
    n = 1000

    for i in range(n):
        queue.push(i)

    assert len(queue) == n

    for i in range(n):
        assert queue.pop() == i

    assert queue.is_empty()


def test_different_data_types():
    queue = Queue()

    queue.push(42)
    queue.push("hello")
    queue.push(3.14)
    queue.push([1, 2, 3])
    queue.push({"key": "value"})

    assert queue.pop() == 42
    assert queue.pop() == "hello"
    assert queue.pop() == 3.14
    assert queue.pop() == [1, 2, 3]
    assert queue.pop() == {"key": "value"}
