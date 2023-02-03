import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "input, output",
    (
        (4, 4),
        (25, 1389537),
    ),
)
def test(input, output):
    tester = Solution()
    assert tester.tribonacci(input) == output
