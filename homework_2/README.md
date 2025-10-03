# Homework 2

A set of three independent tasks implementing data structures and algorithms with linked lists.

## Task Descriptions

### 1) `stack_vs_queue`

**Task:** Implement stack and queue data structures based on linked lists.

**Requirements:**
- Implement both structures without using external libraries
- Stack operations: `push()`, `pop()`, `top()`, `is_empty()`, `__len__()`
- Queue operations: `push()`, `pop()`, `top()`, `is_empty()`, `__len__()`
- Write comprehensive tests using `pytest`

**Stack behavior:** LIFO (Last In First Out)
**Queue behavior:** FIFO (First In First Out)

**Files:**
- `stack.py` - Stack implementation
- `queue.py` - Queue implementation
- `test_stack.py` - Stack tests
- `test_queue.py` - Queue tests

---

### 2) `validate`

**Task:** Given two sequences `pushed` and `popped` containing unique integers, determine whether these sequences could result from a series of push and pop operations on an empty stack.

**Input:** Two sequences of integers
**Output:** `True` or `False`

**Constraints:** `1 <= len(pushed) <= 100_000`

**Example 1:**
```
pushed: [1, 2, 3, 4, 5]
popped: [1, 3, 5, 4, 2]
result: True
```
Operations: `push(1), pop(1), push(2), push(3), pop(3), push(4), push(5), pop(5), pop(4), pop(2)`

**Example 2:**
```
pushed: [1, 2, 3]
popped: [3, 1, 2]
result: False
```
Operations: `push(1), push(2), push(3), pop(3)`, need `pop(1)`, but 2 is on top.

**Requirements:**
- No external libraries
- Write tests using `pytest`

---

### 3) `merge_lists`

**Task:** Given two sorted singly-linked lists `list1` and `list2`, merge them into one new sorted list by splicing together the nodes of the two lists. Return the head of the merged linked list.

**Input:** `list1 = [1,2,4]`, `list2 = [1,3,4]`
**Output:** `[1,1,2,3,4,4]`

**Requirements:**
- Implement **two approaches**: with dummy node and without dummy node
- Write tests using `pytest`

**Files:**
- `list_node.py` - ListNode class and helper functions
- `no_dummy_merge.py` - Solution without dummy node
- `dummy_merge.py` - Solution with dummy node
- `test_merge_lists.py` - Tests for both implementations

---

## Tests

To run the tests for each task, execute the command from the `homework_2` folder:

```bash
pytest ./{task_name}/tests_*.py
```
