import pytest

from .solution import fibonacci


@pytest.mark.parametrize(
    "input, output",
    (
        (5, 5),
        (12, 144),
        (17, 1597),
    ),
)
def test(input, output):
    assert fibonacci(input) == output
