import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "n, output",
    (
        (2, 1),
        (3, 2),
        (4, 3),
    ),
)
def test(n, output):
    tester = Solution()
    assert tester.fib(n) == output
