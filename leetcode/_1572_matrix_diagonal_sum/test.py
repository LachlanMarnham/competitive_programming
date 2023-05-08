import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "mat, result",
    (
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 25),
        ([[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]], 8),
        ([[5]], 5),
    ),
)
def test(mat, result):
    tester = Solution()
    assert tester.diagonal_sum(mat) == result
