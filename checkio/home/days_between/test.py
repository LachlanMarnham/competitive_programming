import pytest

from .solution import days_diff


def checkio_main(a, b, solution):
    assert days_diff(a, b) == solution


@pytest.mark.parametrize('a, b, solution', [
    ((1982, 4, 19), (1982, 4, 22), 3),
    ((2014, 1, 1), (2014, 8, 27), 238),
    ((2014, 8, 27), (2014, 1, 1), 238),
])
def test(a, b, solution):
    checkio_main(a, b, solution)
