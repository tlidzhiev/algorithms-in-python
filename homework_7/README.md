# Homework 7

A set of two independent tasks implementing heap construction algorithms and finding k-th largest element.

## Task Descriptions

### 1) `makeheap`

**Task:** Implement two algorithms to build a min-heap from an arbitrary array with different time complexities.

**Requirements:**
- Implement `makeheap_n_log_n(arr)` - O(N log N) heap construction
- Implement `makeheap(arr)` - O(N) heap construction (Floyd's algorithm)
- Provide mathematical proof of O(N) complexity
- Compare execution times of both methods
- Cannot use built-in libraries

---

### 2) `kth-minheap`

**Task:** Find the k-th largest element in an array using min-heap. Cannot simply sort the array.

**Input:** Array of integers and integer k

**Output:** k-th largest element

**Example 1:**
```
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Explanation: Sorted descending: [6,5,4,3,2,1], 2nd largest is 5
```

**Example 2:**
```
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
Explanation: Sorted descending: [6,5,5,4,3,3,2,2,1], 4th largest is 4
```

**Requirements:**
- Solution WITHOUT heapq (custom heap implementation)
- Solution WITH heapq (Python's built-in)
- Comprehensive tests using pytest

---

## Tests
To run the tests for each task, execute the command from the `homework_7` folder:

```bash
pytest ./{task_name}/tests.py -s
```
