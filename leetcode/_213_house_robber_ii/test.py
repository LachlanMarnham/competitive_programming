import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "nums, result",
    (
        ([2, 3, 2], 3),
        ([1, 2, 3, 1], 4),
        ([1, 2, 3], 3),
    ),
)
def test(nums, result):
    tester = Solution()
    assert tester.rob(nums) == result
