import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "jumps, output",
    (
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
    ),
)
def test(jumps, output):
    assert Solution().jump(jumps) == output
