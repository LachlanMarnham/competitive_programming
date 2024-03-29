import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "nums, n, output",
    (
        ([2, 5, 1, 3, 4, 7], 3, [2, 3, 5, 4, 1, 7]),
        ([1, 2, 3, 4, 4, 3, 2, 1], 4, [1, 4, 2, 3, 3, 2, 4, 1]),
        ([1, 1, 2, 2], 2, [1, 2, 1, 2]),
    ),
)
def test(nums, n, output):
    tester = Solution()
    assert tester.shuffle(nums, n) == output
