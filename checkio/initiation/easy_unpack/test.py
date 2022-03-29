import pytest

from .solution import easy_unpack


def checkio_main(elements, solution):
    assert easy_unpack(elements) == solution


@pytest.mark.parametrize('elements, solution', [
    ((1, 2, 3, 4, 5, 6, 7, 9), (1, 3, 7)),
    ((6, 2, 9, 4, 3, 9), (6, 9, 3)),
    ((1, 1, 1, 1), (1, 1, 1)),
    ((6, 3, 7), (6, 7, 3)),
])
def test(elements, solution):
    checkio_main(elements, solution)
