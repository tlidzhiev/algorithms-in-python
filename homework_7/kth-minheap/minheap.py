class MinHeap:
    def __init__(self, arr=None):
        if arr is None:
            self.heap = []
        else:
            self.heap = arr.copy()
            self._build_heap()

    def _build_heap(self):
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(i)

    def _sift_up(self, index):
        while index > 0:
            parent_idx = (index - 1) // 2
            if self.heap[index] < self.heap[parent_idx]:
                self.heap[index], self.heap[parent_idx] = \
                    self.heap[parent_idx], self.heap[index]
                index = parent_idx
            else:
                break

    def _sift_down(self, index):
        n = len(self.heap)
        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = \
                self.heap[smallest], self.heap[index]
            index = smallest

    def push(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 1:
            return self.heap.pop()

        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)

        return min_val

    def peek(self):
        return self.heap[0]
