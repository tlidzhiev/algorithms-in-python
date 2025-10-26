# Homework 3

A set of independent tasks implementing hash tables and array algorithms.

## Task Descriptions

### 1) `two_sum`

**Task:** Given an array of integers `arr` and an integer `k`, find the indices of two elements whose sum equals `k`.

**Input:** Array of integers and target sum

**Output:** Two indices in ascending order (space-separated)

**Constraints:**
- Guaranteed to have exactly one solution
- Return indices in ascending order

**Example 1:**
```
Input: arr = [1, 3, 4, 10], k = 7
Output: 1 2
Explanation: arr[1] + arr[2] = 3 + 4 = 7
```

**Example 2:**
```
Input: arr = [5, 5, 1, 4], k = 10
Output: 0 1
Explanation: arr[0] + arr[1] = 5 + 5 = 10
```

**Algorithm:**
- Use a hash map to store seen numbers and their indices
- For each number, check if its complement (k - num) exists in the map
- Return indices when complement is found

**Files:**
- `two_sum.py` - Solution implementation
- `test_two_sum.py` - Comprehensive tests
- `README.md` - Task description and usage

---

### 2) `anagrams`

**Task:** Given a list of words, group them so that all anagrams are in the same group.

**Input:** List of strings

**Output:** List of groups, where each group contains anagrams

**Definition:** Anagrams are words that contain the same letters in different order.

**Example:**
```
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
```

**Explanation:**
- "eat", "tea", "ate" are anagrams (all contain letters 'a', 'e', 't')
- "tan", "nat" are anagrams (all contain letters 'a', 'n', 't')
- "bat" is unique


**Algorithm:**
- For each word, create a key by sorting its letters
- Words with the same key are anagrams
- Group words by their sorted key

**Files:**
- `anagrams.py` - Solution implementation
- `test_anagrams.py` - Comprehensive tests
- `README.md` - Task description and examples

---

## Tests

To run the tests for each task, execute the command from the `homework_3` folder:

```bash
pytest ./{task_name}/tests_*.py
```

---
