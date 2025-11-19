def mergesort(arr):
    if len(arr) <= 1:
        return arr

    result = arr.copy()
    n = len(result)
    size = 1

    while size < n:
        for start in range(0, n, size * 2):
            mid = min(start + size, n)
            end = min(start + size * 2, n)

            merge(result, start, mid, end)

        size *= 2

    return result


def merge(arr, start, mid, end):
    left = arr[start:mid]
    right = arr[mid:end]

    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    result = arr.copy()
    stack = [(0, len(result) - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pivot_index = partition(result, low, high)

            stack.append((low, pivot_index - 1))
            stack.append((pivot_index + 1, high))

    return result


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
