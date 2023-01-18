import pytest

from .solution import ListNode, Solution


@pytest.mark.parametrize(
    "input, output",
    (
        ([1, 2, 2, 1], True),
        ([1, 2], False),
    ),
)
def test(input, output):
    tail = head = ListNode(val=input.pop(0))
    for val in input:
        new_node = ListNode(val=val)
        tail.next = new_node
        tail = new_node
    tester = Solution()
    assert tester.is_palindrome(head) == output
