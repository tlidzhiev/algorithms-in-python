import random

from kth_largest_custom import find_kth_largest as find_kth_largest_custom
from kth_largest_heapq import find_kth_largest as find_kth_largest_heapq


def test_provided_examples():
    # Example 1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    expected1 = 5

    result_custom = find_kth_largest_custom(nums1, k1)
    result_heapq = find_kth_largest_heapq(nums1, k1)

    assert result_custom == expected1
    assert result_heapq == expected1

    # Example 2
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    expected2 = 4

    result_custom = find_kth_largest_custom(nums2, k2)
    result_heapq = find_kth_largest_heapq(nums2, k2)

    assert result_custom == expected2
    assert result_heapq == expected2



def test_edge_cases():
    # Single element
    nums = [42]
    k = 1
    result_custom = find_kth_largest_custom(nums, k)
    result_heapq = find_kth_largest_heapq(nums, k)
    assert result_custom == result_heapq == 42

    # Two elements, k=1
    nums = [1, 2]
    k = 1
    result_custom = find_kth_largest_custom(nums, k)
    result_heapq = find_kth_largest_heapq(nums, k)
    assert result_custom == result_heapq == 2

    # Two elements, k=2
    k = 2
    result_custom = find_kth_largest_custom(nums, k)
    result_heapq = find_kth_largest_heapq(nums, k)
    assert result_custom == result_heapq == 1

    nums = [5, 5, 5, 5, 5]
    k = 3
    result_custom = find_kth_largest_custom(nums, k)
    result_heapq = find_kth_largest_heapq(nums, k)
    assert result_custom == result_heapq == 5


def test_boundary_k_values():
    nums = [10, 3, 7, 1, 9, 5]

    # k=1 should return maximum
    k = 1
    result_custom = find_kth_largest_custom(nums, k)
    result_heapq = find_kth_largest_heapq(nums, k)
    expected = 10
    assert result_custom == result_heapq == expected

    # k=n should return minimum
    k = len(nums)
    result_custom = find_kth_largest_custom(nums, k)
    result_heapq = find_kth_largest_heapq(nums, k)
    expected = 1
    assert result_custom == result_heapq == expected

def test_random_arrays():
    sizes = [10, 50, 100, 500]
    num_tests_per_size = 5

    for size in sizes:
        for _ in range(num_tests_per_size):
            nums = [random.randint(-1000, 1000) for _ in range(size)]
            k = random.randint(1, size)

            sorted_desc = sorted(nums, reverse=True)
            expected = sorted_desc[k-1]

            result_custom = find_kth_largest_custom(nums, k)
            result_heapq = find_kth_largest_heapq(nums, k)

            assert result_custom == expected
            assert result_heapq == expected

def test_duplicates():
    nums = [5, 2, 5, 1, 5, 3, 5, 4, 5]
    k = 4
    sorted_desc = sorted(nums, reverse=True)
    expected = sorted_desc[k-1]

    result_custom = find_kth_largest_custom(nums, k)
    result_heapq = find_kth_largest_heapq(nums, k)

    assert result_custom == result_heapq == expected

def test_large_array():
    size = 100000
    nums = [random.randint(1, 1000000) for _ in range(size)]
    k = size // 2

    sorted_desc = sorted(nums, reverse=True)
    expected = sorted_desc[k-1]

    result_custom = find_kth_largest_custom(nums, k)
    result_heapq = find_kth_largest_heapq(nums, k)

    assert result_custom == expected
    assert result_heapq == expected
