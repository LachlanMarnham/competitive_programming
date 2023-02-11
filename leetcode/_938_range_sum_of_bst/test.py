import pytest

from .solution import Solution, TreeNode


@pytest.mark.parametrize(
    "vals, low, high, output",
    (
        ([10, 5, 15, 3, 7, 18], 7, 15, 32),
        ([10, 5, 15, 3, 7, 13, 18, 1, 6], 6, 10, 23),
    ),
)
def test(vals, low, high, output):
    root = TreeNode.from_vals(vals)
    tester = Solution()
    assert tester.range_sum_bst(root, low, high) == output
