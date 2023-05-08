import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "nums, result",
    (
        ([1, 2, 3, 1], 4),
        ([2, 7, 9, 3, 1], 12),
    ),
)
def test(nums, result):
    tester = Solution()
    assert tester.rob(nums) == result
