import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "board, result",
    (
        (
            [
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 35, -1, -1, 13, -1],
                [-1, -1, -1, -1, -1, -1],
                [-1, 15, -1, -1, -1, -1],
            ],
            4,
        ),
        ([[-1, -1], [-1, 3]], 1),
    ),
)
def test(board, result):
    tester = Solution()
    assert tester.snakes_and_ladders(board) == result
