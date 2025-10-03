import pytest
from dummy_merge import merge_two_lists_with_dummy
from list_node import linked_list_to_list, list_to_linked_list
from no_dummy_merge import merge_two_lists_without_dummy


@pytest.mark.parametrize(
    "merge_func", [merge_two_lists_without_dummy, merge_two_lists_with_dummy]
)
@pytest.mark.parametrize(
    "list1, list2, expected",
    [
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),
        ([], [0], [0]),
        ([1], [], [1]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
        ([4, 5, 6], [1, 2, 3], [1, 2, 3, 4, 5, 6]),
        ([1], [1], [1, 1]),
        (None, [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], None, [1, 2, 3]),
        (None, None, []),
        ([1, 1, 1], [1, 1, 1], [1, 1, 1, 1, 1, 1]),
        (list(range(0, 100, 2)), list(range(1, 100, 2)), list(range(100))),
        ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ],
)
def test_merge_two_lists(merge_func, list1, list2, expected):
    l1 = list_to_linked_list(list1) if list1 is not None else None
    l2 = list_to_linked_list(list2) if list2 is not None else None
    result = merge_func(l1, l2)
    assert linked_list_to_list(result) == expected
