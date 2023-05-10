import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "nums, output",
    (
        ([3, 4, 2], 6),
        ([2, 2, 3, 3, 3, 4], 9),
    ),
)
def test(nums, output):
    assert Solution().delete_and_earn(nums) == output
