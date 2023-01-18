import pytest

from .solution import beginning_zeros


def checkio_main(number, solution):
    assert beginning_zeros(number) == solution


@pytest.mark.parametrize(
    "number, solution",
    [
        ("100", 0),
        ("001", 2),
        ("100100", 0),
        ("001001", 2),
        ("012345679", 1),
        ("0000", 4),
    ],
)
def test(number, solution):
    checkio_main(number, solution)
