from typing import List, Optional


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def add(self, val: int) -> None:
        if val < self.val:
            if self.left is None:
                self.left = TreeNode(val)
            else:
                self.left.add(val)
        else:
            if self.right is None:
                self.right = TreeNode(val)
            else:
                self.right.add(val)

    @classmethod
    def from_vals(cls, vals: List[int]) -> "TreeNode":
        root = cls(vals.pop(0))
        for val in vals:
            root.add(val)
        return root


class Solution:
    def range_sum_bst(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node is not None:
                if low <= node.val <= high:
                    result += node.val
                if node.val > low:
                    stack.append(node.left)
                if node.val < high:
                    stack.append(node.right)
        return result
