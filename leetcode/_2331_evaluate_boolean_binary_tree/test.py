import pytest

from .solution import TreeNode, Solution


@pytest.mark.parametrize('data, output', (
    ([2,1,3,None,None,0,1], True),
    ([0], False),
))
def test(data, output):
    root = TreeNode.from_data(data)
    assert Solution().evaluate_tree(root) == output
