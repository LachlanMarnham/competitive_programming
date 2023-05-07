import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "nums, target, result",
    (([3, 5, 6, 7], 9, 4), ([3, 3, 6, 8], 10, 6), ([2, 3, 3, 4, 6, 7], 12, 61)),
)
def test(nums, target, result):
    tester = Solution()
    assert tester.num_subseq(nums, target) == result
