import pytest

from .solution import number_length


def checkio_main(a, solution):
    assert number_length(a) == solution


@pytest.mark.parametrize(
    "a, solution",
    [
        (10, 2),
        (0, 1),
        (4, 1),
        (44, 2),
    ],
)
def test(a, solution):
    checkio_main(a, solution)
