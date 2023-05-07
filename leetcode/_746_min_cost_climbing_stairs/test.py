import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "cost, result",
    (([10, 15, 20], 15), ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6)),
)
def test(cost, result):
    tester = Solution()
    assert tester.min_cost_climbing_stairs(cost) == result
