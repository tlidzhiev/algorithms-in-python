from minheap import MinHeap


def find_kth_largest(nums, k):
    heap = MinHeap(nums[:k])
    for i in range(k, len(nums)):
        if nums[i] > heap.peek():
            heap.pop()
            heap.push(nums[i])
    return heap.peek()
