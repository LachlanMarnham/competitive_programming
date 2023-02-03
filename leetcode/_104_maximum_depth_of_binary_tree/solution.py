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
    depth: int


class Solution:
    def max_depth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        max_depth = 0
        start_item = StackItem(node=root, depth=1)
        stack = [start_item]
        while stack:
            next_item = stack.pop()
            node = next_item.node
            depth = next_item.depth
            if depth > max_depth:
                max_depth = depth
            if node.left is not None:
                left_item = StackItem(node=node.left, depth=depth + 1)
                stack.append(left_item)
            if node.right is not None:
                right_item = StackItem(node=node.right, depth=depth + 1)
                stack.append(right_item)
        return max_depth
