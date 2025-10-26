from main import two_sum


def test_example_1():
    arr = [1, 3, 4, 10]
    k = 7
    result = two_sum(arr, k)
    assert result == (1, 2), f"Expected (1, 2), got {result}"
    assert arr[result[0]] + arr[result[1]] == k


def test_example_2():
    arr = [5, 5, 1, 4]
    k = 10
    result = two_sum(arr, k)
    assert result == (0, 1), f"Expected (0, 1), got {result}"
    assert arr[result[0]] + arr[result[1]] == k


def test_pair_at_start():
    arr = [2, 7, 11, 15]
    k = 9
    result = two_sum(arr, k)
    assert result == (0, 1)
    assert arr[result[0]] + arr[result[1]] == k


def test_pair_at_end():
    arr = [1, 2, 3, 4, 5, 9]
    k = 14
    result = two_sum(arr, k)
    assert result == (4, 5)
    assert arr[result[0]] + arr[result[1]] == k


def test_pair_far_apart():
    arr = [10, 1, 2, 3, 4, 5]
    k = 15
    result = two_sum(arr, k)
    assert result == (0, 5)
    assert arr[result[0]] + arr[result[1]] == k


def test_with_zero():
    arr = [0, 4, 3, 0]
    k = 0
    result = two_sum(arr, k)
    assert result == (0, 3)
    assert arr[result[0]] + arr[result[1]] == k


def test_two_elements():
    arr = [1, 2]
    k = 3
    result = two_sum(arr, k)
    assert result == (0, 1)
    assert arr[result[0]] + arr[result[1]] == k


def test_order_of_indices():
    arr = [3, 2, 4]
    k = 6
    result = two_sum(arr, k)
    assert result[0] < result[1], "Indices must be in ascending order"
    assert arr[result[0]] + arr[result[1]] == k
