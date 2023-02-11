import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "inputs, output",
    (
        (["coffee", "donuts", "time", "toffee"], 6),
        (["lack", "back"], 0),
    ),
)
def test(inputs, output):
    assert Solution().distinct_names(inputs) == output
