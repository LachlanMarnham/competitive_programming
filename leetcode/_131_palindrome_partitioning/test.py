import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "input, output",
    (
        ("aab", [["a", "a", "b"], ["aa", "b"]]),
        ("a", [["a"]]),
    ),
)
def test(input, output):
    solver = Solution()
    assert solver.partition(input) == output
