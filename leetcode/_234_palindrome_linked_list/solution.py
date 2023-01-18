from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def is_palindrome(self, head: Optional[ListNode]) -> bool:
        stack = []
        node = head
        while node is not None:
            stack.append(node.val)
            node = node.next

        node = head
        while len(stack) > 0:
            val = stack.pop()
            if val != node.val:
                return False
            node = node.next
        return True
