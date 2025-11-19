# Homework 6

A set of three independent tasks implementing recursive and iterative sorting algorithms, performance comparison, and quickselect algorithm.

## Task Descriptions

### 1) `compare`

**Task:** Implement recursive versions of mergesort and quicksort with a timing decorator.

**Files:**
- `main.py` - Recursive sorting algorithms with timer decorator
- `tests.py` - Correctness and performance tests

---

### 2) `iterative`

**Task:** Implement iterative versions of mergesort and quicksort.

**Files:**
- `main.py` - Iterative sorting implementations
- `tests.py` - Tests for edge cases and large arrays

---

### 3) `kth`

**Task:** Find the k-th largest element in an array using quickselect algorithm.

**Input:** `nums = [3,2,1,5,6,4], k = 2`
**Output:** `5`

**Additional example:**
- Input: `nums = [3,2,3,1,2,4,5,5,6], k = 4` → Output: `4`

**Files:**
- `main.py` - Quickselect implementation
- `tests.py` - Tests including provided examples

---

## Tests

To run the tests for each task, execute the command from the `homework_6` folder:

```bash
pytest ./{task_name}/tests.py -v
```
