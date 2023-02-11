from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def _create_binary_tree(self, data: list, index: int) -> "TreeNode":
        node = None
        if index < len(data):
            if data[index] is None:
                return
            node = TreeNode(data[index])
            node.left = self._create_binary_tree(data, 2 * index + 1)
            node.right = self._create_binary_tree(data, 2 * index + 2)
        return node

    @classmethod
    def from_data(cls, data: list):
        return cls()._create_binary_tree(data, 0)


class Solution:
    def evaluate_tree(self, root: Optional[TreeNode]) -> bool:
        if root.left is None:
            return root.val
        left = self.evaluate_tree(root.left)
        right = self.evaluate_tree(root.right)
        if root.val == 2:
            return left or right
        else:
            return left and right
