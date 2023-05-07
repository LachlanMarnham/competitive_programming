import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "nums_1, nums_2, result",
    (
        ([1, 2, 3], [2, 4, 6], [[1, 3], [4, 6]]),
        ([1, 2, 3, 3], [1, 1, 2, 2], [[3], []]),
    ),
)
def test(nums_1, nums_2, result):
    tester = Solution()
    assert tester.find_difference(nums_1, nums_2) == result
