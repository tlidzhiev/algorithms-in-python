import random
from collections import Counter

import pytest
from makeheap import makeheap, makeheap_n_log_n


def is_min_heap(arr):
    n = len(arr)

    for i in range(n // 2):
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and arr[i] > arr[left_child]:
            return False

        if right_child < n and arr[i] > arr[right_child]:
            return False

    return True


@pytest.mark.parametrize("arr_input,expected", [
    ([], []),
    ([42], [42]),
])
def test_edge_cases(arr_input, expected):
    arr1 = arr_input.copy()
    arr2 = arr_input.copy()

    result1 = makeheap_n_log_n(arr1)
    result2 = makeheap(arr2)

    assert result1 == expected
    assert result2 == expected
    assert is_min_heap(result1)
    assert is_min_heap(result2)


@pytest.mark.parametrize("arr_input,expected_min", [
    ([1, 2], 1),
    ([2, 1], 1),
    ([5, 3], 3),
    ([10, 20], 10),
    ([-1, -2], -2),
    ([0, 1], 0),
])
def test_two_elements(arr_input, expected_min):
    arr1 = arr_input.copy()
    arr2 = arr_input.copy()

    makeheap_n_log_n(arr1)
    makeheap(arr2)

    assert is_min_heap(arr1)
    assert is_min_heap(arr2)
    assert arr1[0] == expected_min
    assert arr2[0] == expected_min


@pytest.mark.parametrize("arr_input,expected_min", [
    ([1, 2, 3], 1),
    ([3, 2, 1], 1),
    ([2, 1, 3], 1),
    ([5, 3, 7, 1, 9], 1),
    ([10, 5, 20, 1, 15], 1),
])
def test_small_arrays(arr_input, expected_min):
    arr1 = arr_input.copy()
    arr2 = arr_input.copy()

    makeheap_n_log_n(arr1)
    makeheap(arr2)

    assert is_min_heap(arr1)
    assert is_min_heap(arr2)
    assert arr1[0] == expected_min
    assert arr2[0] == expected_min


@pytest.mark.parametrize("arr_input,expected_min", [
    ([1, 2, 3, 4, 5, 6, 7], 1),
    ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 1),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1),
    ([5, 4, 3, 2, 1], 1),
    ([1, 3, 5, 7, 9], 1),
])
def test_sorted_arrays(arr_input, expected_min):
    arr1 = arr_input.copy()
    arr2 = arr_input.copy()

    makeheap_n_log_n(arr1)
    makeheap(arr2)

    assert is_min_heap(arr1)
    assert is_min_heap(arr2)
    assert arr1[0] == expected_min
    assert arr2[0] == expected_min


@pytest.mark.parametrize("arr_input,expected_min", [
    ([5, 5, 5, 5, 5], 5),
    ([5, 5, 5, 5, 5, 5, 5], 5),
    ([1, 1, 1], 1),
    ([0, 0, 0, 0], 0),
    ([-3, -3, -3], -3),
])
def test_all_duplicates(arr_input, expected_min):
    arr1 = arr_input.copy()
    arr2 = arr_input.copy()

    makeheap_n_log_n(arr1)
    makeheap(arr2)

    assert is_min_heap(arr1)
    assert is_min_heap(arr2)
    assert arr1[0] == expected_min
    assert arr2[0] == expected_min
    assert all(x == expected_min for x in arr1)


@pytest.mark.parametrize("arr_input,expected_min", [
    ([3, 1, 4, 1, 5, 9, 2, 6, 5, 3], 1),
    ([5, 2, 5, 1, 5, 3, 5], 1),
    ([7, 7, 3, 3, 1, 1], 1),
    ([10, 5, 10, 5, 10], 5),
])
def test_some_duplicates(arr_input, expected_min):
    arr1 = arr_input.copy()
    arr2 = arr_input.copy()

    makeheap_n_log_n(arr1)
    makeheap(arr2)

    assert is_min_heap(arr1)
    assert is_min_heap(arr2)
    assert arr1[0] == expected_min
    assert arr2[0] == expected_min
    assert sorted(arr1) == sorted(arr2)
