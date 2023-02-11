from dataclasses import dataclass
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


@dataclass
class StackItem:
    node: Optional[TreeNode]
    depth: int


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        root_item = StackItem(node=root, depth=1)
        stack = [root_item]
        total = 0
        max_depth = 1

        while stack:
            item = stack.pop()
            node, depth = item.node, item.depth
            if node is not None:
                left_node = node.left
                right_node = node.right
                left_item = StackItem(node=left_node, depth=depth + 1)
                right_item = StackItem(node=right_node, depth=depth + 1)
                stack.append(left_item)
                stack.append(right_item)

                # If it is a leaf...
                if left_node is None and right_node is None:
                    # At the current maximum depth...
                    if depth == max_depth:
                        total += node.val
                    # ...Or if we've reached a new maximum depth
                    elif depth > max_depth:
                        max_depth = depth
                        total = node.val
        return total
