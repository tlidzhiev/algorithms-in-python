from typing import Any


class ListNode:
    def __init__(self, val: Any, next: Any | None = None):
        self.val = val
        self.next = next


def list_to_linked_list(lst: list[Any]) -> ListNode | None:
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def linked_list_to_list(head: ListNode | None) -> list[Any]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result
