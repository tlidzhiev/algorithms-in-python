def _sift_up(arr, index):
    while index > 0:
        parent_index = (index - 1) // 2
        if arr[index] < arr[parent_index]:
            arr[index], arr[parent_index] = arr[parent_index], arr[index]
            index = parent_index
        else:
            break


def _sift_down(arr, index, heap_size):
    while True:
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < heap_size and arr[left_child] < arr[smallest]:
            smallest = left_child

        if right_child < heap_size and arr[right_child] < arr[smallest]:
            smallest = right_child

        if smallest == index:
            break

        arr[index], arr[smallest] = arr[smallest], arr[index]
        index = smallest


def makeheap_n_log_n(arr):
    if len(arr) <= 1:
        return arr

    for i in range(1, len(arr)):
        _sift_up(arr, i)
    return arr


def makeheap(arr):
    if len(arr) <= 1:
        return arr

    n = len(arr)
    start_index = n // 2 - 1
    for i in range(start_index, -1, -1):
        _sift_down(arr, i, n)
    return arr
