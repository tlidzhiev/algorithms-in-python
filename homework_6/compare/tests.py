from main import mergesort, quicksort


def test_mergesort_empty():
    result, _ = mergesort([])
    assert result == []


def test_mergesort_single():
    result, _ = mergesort([5])
    assert result == [5]


def test_mergesort_sorted():
    result, _ = mergesort([1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5]


def test_mergesort_reverse():
    result, _ = mergesort([5, 4, 3, 2, 1])
    assert result == [1, 2, 3, 4, 5]


def test_mergesort_duplicates():
    result, _ = mergesort([3, 1, 4, 1, 5, 9, 2, 6, 5])
    assert result == [1, 1, 2, 3, 4, 5, 5, 6, 9]


def test_quicksort_empty():
    result, _ = quicksort([])
    assert result == []


def test_quicksort_single():
    result, _ = quicksort([5])
    assert result == [5]


def test_quicksort_sorted():
    result, _ = quicksort([1, 2, 3, 4, 5])
    assert result == [1, 2, 3, 4, 5]


def test_quicksort_reverse():
    result, _ = quicksort([5, 4, 3, 2, 1])
    assert result == [1, 2, 3, 4, 5]


def test_quicksort_duplicates():
    result, _ = quicksort([3, 1, 4, 1, 5, 9, 2, 6, 5])
    assert result == [1, 1, 2, 3, 4, 5, 5, 6, 9]
