import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "n, trust, output",
    (
        (2, [[1, 2]], 2),
        (3, [[1, 3], [2, 3]], 3),
        (3, [[1, 3], [2, 3], [3, 1]], -1),
    ),
)
def test(n, trust, output):
    tester = Solution()
    assert tester.find_judge(n, trust) == output
