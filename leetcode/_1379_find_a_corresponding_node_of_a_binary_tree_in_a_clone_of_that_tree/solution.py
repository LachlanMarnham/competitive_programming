class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def get_cloned_target(self, node: TreeNode, target_value: int) -> TreeNode:
        if node.val == target_value:
            return node
        if node.left is not None:
            left_search = self.get_cloned_target(node.left, target_value)
            if left_search is not None:
                return left_search
        if node.right is not None:
            right_search = self.get_cloned_target(node.right, target_value)
            if node.right is not None:
                return right_search

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        target_value = target.val
        return self.get_cloned_target(cloned, target_value)
