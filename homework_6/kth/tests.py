from main import find_kth_largest


def test_example_1():
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    assert find_kth_largest(nums, k) == 5


def test_example_2():
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    assert find_kth_largest(nums, k) == 4


def test_single_element():
    assert find_kth_largest([5], 1) == 5


def test_first_largest():
    nums = [3, 2, 1, 5, 6, 4]
    assert find_kth_largest(nums, 1) == 6


def test_last_largest():
    nums = [3, 2, 1, 5, 6, 4]
    assert find_kth_largest(nums, 6) == 1


def test_duplicates():
    nums = [1, 1, 1, 1]
    assert find_kth_largest(nums, 2) == 1


def test_two_elements():
    assert find_kth_largest([1, 2], 1) == 2
    assert find_kth_largest([1, 2], 2) == 1


def test_sorted_array():
    nums = [1, 2, 3, 4, 5]
    assert find_kth_largest(nums, 3) == 3


def test_reverse_sorted():
    nums = [5, 4, 3, 2, 1]
    assert find_kth_largest(nums, 3) == 3
