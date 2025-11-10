# Homework 5

A set of three independent tasks implementing recursion tracing, permutation algorithms, and self-balancing trees.

## Task Descriptions

### 1) `tracer`

**Task:** Implement a decorator that visualizes the call stack of recursive functions.

**Requirements:**
- Show function entry with arguments
- Display indentation corresponding to stack depth
- Show function exit with return value
- Write tests using `pytest`

**Example output:**
```
-> factorial(5)
  -> factorial(4)
    -> factorial(3)
      -> factorial(2)
        -> factorial(1)
        <- factorial(1) = 1
      <- factorial(2) = 2
    <- factorial(3) = 6
  <- factorial(4) = 24
<- factorial(5) = 120
```

**Files:**
- `main.py` - Tracer decorator implementation
- `tests.py` - Tests with factorial, fibonacci, and gcd examples

---

### 2) `permutations`

**Task:** Given an array, return all possible permutations.

**Input:** `nums = [1,2,3]`
**Output:** `[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]`

**Additional examples:**
- Input: `nums = [0,1]` → Output: `[[0,1],[1,0]]`
- Input: `nums = [1]` → Output: `[[1]]`

**Requirements:**
- Implement using backtracking algorithm
- Include call stack visualization using the tracer decorator
- Write comprehensive tests using `pytest`

**Algorithm:** Backtracking with recursive exploration of all possibilities

**Complexity:**
- Time: O(n! × n)
- Space: O(n! × n)

**Files:**
- `main.py` - Permutation algorithm with tracer
- `tests.py` - Tests for various input sizes

---

### 3) `avl`

**Task:** Implement an AVL tree class with support for insert, delete, and search operations.

**AVL Property:** For every node, the height difference between left and right subtrees does not exceed 1.

**Required operations:**
- `insert(key)` - Insert element
- `delete(key)` - Delete element
- `search(key)` - Search for element
- `inorder()` - In-order traversal (sorted)
- `is_balanced()` - Check if tree is balanced
- `get_height()` - Get tree height

**Balancing:** Uses four types of rotations:
1. **Left-Left (LL)** → Right rotation
2. **Right-Right (RR)** → Left rotation
3. **Left-Right (LR)** → Left rotation + Right rotation
4. **Right-Left (RL)** → Right rotation + Left rotation

**Complexity:**
- Search: O(log n)
- Insert: O(log n)
- Delete: O(log n)
- Space: O(n)

**Files:**
- `main.py` - AVL tree implementation
- `tests.py` - Comprehensive tests (29 tests total)

---

## Tests

To run the tests for each task, execute the command from the `homework_5` folder:

```bash
pytest ./{task_name}/tests.py -s
```
