import functools
import time


def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        elapsed = end - start
        return result, elapsed
    return wrapper


@timer
def mergesort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left, _ = mergesort(arr[:mid])
    right, _ = mergesort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


@timer
def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    left_sorted, _ = quicksort(left)
    right_sorted, _ = quicksort(right)

    return left_sorted + middle + right_sorted
