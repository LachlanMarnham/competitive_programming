import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "n, result",
    (
        (2, 2),
        (3, 3),
    ),
)
def test(n, result):
    tester = Solution()
    assert tester.climb_stairs(n) == result
