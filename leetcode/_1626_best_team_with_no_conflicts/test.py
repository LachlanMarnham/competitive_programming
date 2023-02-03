import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "scores, ages, output",
    (
        ([1, 3, 5, 10, 15], [1, 2, 3, 4, 5], 34),
        ([4, 5, 6, 5], [2, 1, 2, 1], 16),
        ([1, 2, 3, 5], [8, 9, 10, 1], 6),
    ),
)
def test(scores, ages, output):
    tester = Solution()
    assert tester.best_team_score(scores, ages) == output
