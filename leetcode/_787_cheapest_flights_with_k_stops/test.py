import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "flights, src, dst, k, solution",
    (
        ([[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3, 1, 700),
        ([[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1, 200),
        ([[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0, 500),
    ),
)
def test(flights, src, dst, k, solution):
    tester = Solution()
    assert tester.find_cheapest_price(flights, src, dst, k) == solution
