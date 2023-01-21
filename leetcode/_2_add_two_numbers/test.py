from typing import List

import pytest

from .solution import ListNode, Solution


def linked_list_to_list(linked_list: ListNode) -> List[int]:
    result = []
    while linked_list is not None:
        result.append(linked_list.val)
        linked_list = linked_list.next
    return result


def list_to_linked_list(arr: List[int]) -> ListNode:
    head = tail = ListNode(arr.pop(0))
    while arr:
        node = ListNode(arr.pop(0))
        tail.next = node
        tail = node
    return head


@pytest.mark.parametrize(
    "input_1, input_2, output",
    (
        ([2, 4, 3], [5, 6, 4], [7, 0, 8]),
        ([0], [0], [0]),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    ),
)
def test(input_1, input_2, output):
    solver = Solution()
    list_1 = list_to_linked_list(input_1)
    list_2 = list_to_linked_list(input_2)
    result = solver.add_two_numbers(list_1, list_2)
    assert linked_list_to_list(result) == output
