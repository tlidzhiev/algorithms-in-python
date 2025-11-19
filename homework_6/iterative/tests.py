from main import mergesort, quicksort


def test_mergesort_empty():
    assert mergesort([]) == []


def test_mergesort_single():
    assert mergesort([5]) == [5]


def test_mergesort_sorted():
    assert mergesort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_mergesort_reverse():
    assert mergesort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_mergesort_duplicates():
    assert mergesort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]


def test_mergesort_large():
    arr = [100, 50, 25, 75, 10, 90, 30, 60, 40, 80]
    assert mergesort(arr) == [10, 25, 30, 40, 50, 60, 75, 80, 90, 100]

def test_quicksort_empty():
    assert quicksort([]) == []


def test_quicksort_single():
    assert quicksort([5]) == [5]


def test_quicksort_sorted():
    assert quicksort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_quicksort_reverse():
    assert quicksort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_quicksort_duplicates():
    assert quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5]) == [1, 1, 2, 3, 4, 5, 5, 6, 9]


def test_quicksort_large():
    arr = [100, 50, 25, 75, 10, 90, 30, 60, 40, 80]
    assert quicksort(arr) == [10, 25, 30, 40, 50, 60, 75, 80, 90, 100]


def test_both_algorithms_consistency():
    arr = [7, 2, 9, 1, 5, 3, 8, 4, 6]
    assert mergesort(arr) == quicksort(arr)


def test_large_array():
    arr = list(range(1000, 0, -1))
    expected = list(range(1, 1001))
    assert mergesort(arr) == expected
    assert quicksort(arr) == expected
