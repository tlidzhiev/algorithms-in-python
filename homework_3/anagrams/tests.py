from main import group_anagrams


def test_example_from_task():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = group_anagrams(strs)

    result_sorted = [sorted(group) for group in result]
    result_sorted.sort()

    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    expected_sorted = [sorted(group) for group in expected]
    expected_sorted.sort()

    assert result_sorted == expected_sorted


def test_empty_list():
    strs = []
    result = group_anagrams(strs)
    assert result == []


def test_single_word():
    strs = ["hello"]
    result = group_anagrams(strs)
    assert result == [["hello"]]


def test_no_anagrams():
    strs = ["abc", "def", "ghi"]
    result = group_anagrams(strs)
    assert len(result) == 3
    assert all(len(group) == 1 for group in result)


def test_all_anagrams():
    strs = ["abc", "bca", "cab", "acb"]
    result = group_anagrams(strs)
    assert len(result) == 1
    assert sorted(result[0]) == sorted(strs)


def test_multiple_groups():
    strs = ["listen", "silent", "hello", "world", "enlist"]
    result = group_anagrams(strs)

    listen_group = None
    for group in result:
        if "listen" in group:
            listen_group = sorted(group)
            break

    assert listen_group == ["enlist", "listen", "silent"]


def test_single_letter_words():
    strs = ["a", "b", "a", "c", "b"]
    result = group_anagrams(strs)

    result_sorted = [sorted(group) for group in result]
    result_sorted.sort()

    assert len(result) == 3


def test_empty_strings():
    strs = ["", "", "a"]
    result = group_anagrams(strs)

    empty_group = None
    for group in result:
        if "" in group:
            empty_group = group
            break

    assert empty_group == ["", ""]


def test_repeated_letters():
    strs = ["aab", "aba", "baa", "abc"]
    result = group_anagrams(strs)

    assert len(result) == 2

    aab_group = None
    for group in result:
        if "aab" in group:
            aab_group = sorted(group)
            break

    assert aab_group == ["aab", "aba", "baa"]


def test_case_sensitive():
    strs = ["Eat", "eat", "Tea", "tea"]
    result = group_anagrams(strs)

    # "Eat" and "eat" are different words due to case
    # Must be only 3 groups: ["Eat"], ["Tea"] и ["eat", "tea"]
    assert len(result) == 3
