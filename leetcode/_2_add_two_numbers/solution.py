class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, list_1: ListNode, list_2: ListNode) -> ListNode:
        node_1 = list_1
        node_2 = list_2
        remainder, val = divmod(node_1.val + node_2.val, 10)
        result_head = result_tail = ListNode(val)
        while node_1.next or node_2.next or remainder:
            if node_1.next is not None:
                node_1 = node_1.next
                val_1 = node_1.val
            else:
                val_1 = 0
            if node_2.next is not None:
                node_2 = node_2.next
                val_2 = node_2.val
            else:
                val_2 = 0
            remainder, val = divmod(val_1 + val_2 + remainder, 10)
            new_node = ListNode(val)
            result_tail.next = new_node
            result_tail = new_node
        return result_head
