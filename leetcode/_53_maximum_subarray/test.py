import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "nums, output",
    (
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
    ),
)
def test(nums, output):
    assert Solution().max_sub_array(nums) == output
