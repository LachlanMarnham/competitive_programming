import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "nums, output",
    (
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
    ),
)
def test(nums, output):
    assert Solution().can_jump(nums) == output
