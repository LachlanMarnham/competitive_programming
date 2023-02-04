from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, node, output):
        if node:
            self.dfs(node.left, output)
            output.append(node.val)
            self.dfs(node.right, output)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        self.dfs(root, output)
        return output
