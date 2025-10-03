import pytest
from stack import Stack


def test_stack_creation():
    stack = Stack()
    assert stack.is_empty()
    assert len(stack) == 0


@pytest.mark.parametrize(
    "elements, expected_size, expected_top",
    [
        ([1], 1, 1),
        ([1, 2], 2, 2),
        ([1, 2, 3], 3, 3),
        ([5, 10, 15, 20], 4, 20),
        (["a", "b", "c"], 3, "c"),
    ],
)
def test_push_elements(elements, expected_size, expected_top):
    stack = Stack()
    for elem in elements:
        stack.push(elem)
    assert not stack.is_empty()
    assert len(stack) == expected_size
    assert stack.top() == expected_top


@pytest.mark.parametrize(
    "elements, expected_order",
    [
        ([1, 2, 3], [3, 2, 1]),
        ([5, 10, 15], [15, 10, 5]),
        (["x", "y", "z"], ["z", "y", "x"]),
        ([42], [42]),
    ],
)
def test_pop_elements(elements, expected_order):
    stack = Stack()
    for elem in elements:
        stack.push(elem)

    result = []
    while not stack.is_empty():
        result.append(stack.pop())

    assert result == expected_order
    assert stack.is_empty()
    assert len(stack) == 0


@pytest.mark.parametrize(
    "operation, error_message",
    [
        ("pop", "Pop from empty stack"),
        ("top", "Peek from empty stack"),
    ],
)
def test_empty_stack_operations(operation, error_message):
    stack = Stack()
    with pytest.raises(IndexError, match=error_message):
        getattr(stack, operation)()


def test_top_does_not_remove_element():
    stack = Stack()
    stack.push(10)
    stack.push(20)

    assert stack.top() == 20
    assert len(stack) == 2
    assert stack.top() == 20
    assert len(stack) == 2


def test_lifo_behavior():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_alternating_operations():
    stack = Stack()

    stack.push(1)
    assert stack.pop() == 1

    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3

    stack.push(4)
    assert stack.pop() == 4
    assert stack.pop() == 2


def test_size_tracking():
    stack = Stack()

    assert len(stack) == 0

    stack.push(1)
    assert len(stack) == 1

    stack.push(2)
    stack.push(3)
    assert len(stack) == 3

    stack.pop()
    assert len(stack) == 2

    stack.pop()
    stack.pop()
    assert len(stack) == 0


def test_large_number_of_elements():
    stack = Stack()
    n = 1000

    for i in range(n):
        stack.push(i)

    assert len(stack) == n

    for i in range(n - 1, -1, -1):
        assert stack.pop() == i

    assert stack.is_empty()


def test_different_data_types():
    stack = Stack()

    stack.push(42)
    stack.push("hello")
    stack.push(3.14)
    stack.push([1, 2, 3])
    stack.push({"key": "value"})

    assert stack.pop() == {"key": "value"}
    assert stack.pop() == [1, 2, 3]
    assert stack.pop() == 3.14
    assert stack.pop() == "hello"
    assert stack.pop() == 42
