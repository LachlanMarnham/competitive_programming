import pytest

from .solution import even_last


def checkio_main(array, solution):
    assert even_last(array) == solution


@pytest.mark.parametrize('array, solution', [
    ([0, 1, 2, 3, 4, 5], 30),
    ([1, 3, 5], 30),
    ([6], 36),
    ([], 0),
])
def test(array, solution):
    checkio_main(array, solution)
