import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "nums, target, output",
    (
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ),
)
def test(nums, target, output):
    solver = Solution()
    assert solver.two_sum(nums, target).sort() == output.sort()
