import pytest
from main import validate_stack_sequences


@pytest.mark.parametrize(
    "pushed, popped, expected",
    [
        ([1], [1], True),  # минимальный случай
        ([1, 2], [1, 2], True),  # последовательный порядок
        ([1, 2], [2, 1], True),  # обратный порядок
        ([1, 2, 3], [1, 2, 3], True),  # последовательный
        ([1, 2, 3], [3, 2, 1], True),  # обратный
        ([1, 2, 3], [2, 1, 3], True),  # смешанный валидный
        ([1, 2, 3], [2, 3, 1], True),  # смешанный валидный
        ([1, 2, 3], [1, 3, 2], True),  # извлечь из середины
        ([1, 2, 3, 4, 5], [1, 3, 5, 4, 2], True),  # пример 1 из условия
    ],
)
def test_valid_sequences(pushed, popped, expected):
    assert validate_stack_sequences(pushed, popped) == expected


@pytest.mark.parametrize(
    "pushed, popped, expected",
    [
        ([1, 2, 3], [3, 1, 2], False),  # пример 2 из условия
        ([1, 2, 3, 4], [4, 2, 3, 1], False),  # нарушен порядок стека
        ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False),  # невозможная комбинация
        ([1, 2, 3, 4, 5], [4, 5, 3, 1, 2], False),  # нарушен порядок извлечения
    ],
)
def test_invalid_sequences(pushed, popped, expected):
    assert validate_stack_sequences(pushed, popped) == expected


def test_max_length_boundary():
    n = 1000
    pushed = list(range(1, n + 1))
    popped = list(range(n, 0, -1))
    result = validate_stack_sequences(pushed, popped)
    assert isinstance(result, bool)
    assert result


def test_alternating_immediate_pops():
    """Немедленные pop после каждого push"""
    pushed = [1, 2, 3, 4, 5]
    popped = [1, 2, 3, 4, 5]
    assert validate_stack_sequences(pushed, popped)


def test_all_pushes_then_all_pops():
    """Все push, затем все pop"""
    pushed = [1, 2, 3, 4, 5]
    popped = [5, 4, 3, 2, 1]
    assert validate_stack_sequences(pushed, popped)
