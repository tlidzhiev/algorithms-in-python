# Homework 1

A set of three independent tasks with console input and tests using `pytest`.

## Task Descriptions

### 1) `palindrome`
**Task:** Given an integer `N`, determine whether it is a palindrome.

**Restriction:** solve **without using strings**.

**Input:** one integer `N`.

**Output:** `True` or `False`.

### 2) `prime`
**Task:** Given an integer `N`, find the number of prime numbers strictly less than `N` (i.e. compute π(N) for “< N”).

**Input:** one integer `N`.

**Output:** one integer — the count of primes < `N`.

### 3) `sum`
**Task:** Given an array of positive integers, find the **maximum even** sum of a subset of its elements.

**Input:** numbers separated by spaces in a single line.

**Output:** one integer — the required sum.

---

### Tests

To run the tests for each task, execute the command from the `homework_1` folder:

```bash
pytest ./{task_name}/tests.py
```
