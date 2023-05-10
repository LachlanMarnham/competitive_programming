import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "heights, output",
    (
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
    ),
)
def test(heights, output):
    assert Solution().trap(heights) == output
