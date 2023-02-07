import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "fruits, result",
    (
        ([1, 2, 1], 3),
        ([0, 1, 2, 2], 3),
        ([1, 2, 3, 2, 2], 4),
    ),
)
def test(fruits, result):
    tester = Solution()
    assert tester.total_fruit(fruits) == result
