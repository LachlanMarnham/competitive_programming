import pytest

from .solution import max_digit


def checkio_main(items, solution):
    assert max_digit(items) == solution


@pytest.mark.parametrize('items, solution', [
    (0, 0),
    (52, 5),
    (634, 6),
    (1, 1),
    (10000, 1),
])
def test(items, solution):
    checkio_main(items, solution)
