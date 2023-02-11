from dataclasses import dataclass
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


@dataclass
class StackItem:
    node: TreeNode
    high: int
    low: int


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        item = StackItem(node=root, low=-float("inf"), high=float("inf"))
        stack = [item]
        while stack:
            item = stack.pop()
            node, low, high = item.node, item.low, item.high
            left, right = node.left, node.right
            if left is not None:
                if low < left.val < node.val:
                    stack.append(StackItem(node=left, low=low, high=node.val))
                else:
                    return False
            if right is not None:
                if node.val < right.val < high:
                    stack.append(StackItem(node=right, low=node.val, high=high))
                else:
                    return False
        return True
