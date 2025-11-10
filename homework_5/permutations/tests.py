import math

from main import permutations


def test_permutations_different_sizes():
    test_cases = [
        ([], 1, [[]]),
        ([1], 1, [[1]]),
        ([0, 1], 2, [[0, 1], [1, 0]]),
        ([1, 2, 3], 6, [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
        ([1, 2, 3, 4], 24, None),
        ([1, 2, 3, 4, 5], 120, None),
    ]

    for nums, expected_count, expected_perms in test_cases:
        print(f'Permutations for {nums}')
        result = permutations(nums)

        assert len(result) == expected_count
        assert len(result) == math.factorial(len(nums))

        assert len(result) == len(set(tuple(p) for p in result))

        if expected_perms:
            for perm in expected_perms:
                assert perm in result
        print()

def test_permutations_strings():
    nums = ['a', 'b', 'c']
    result = permutations(nums)

    assert len(result) == 6
    assert ['a', 'b', 'c'] in result
    assert ['c', 'b', 'a'] in result
