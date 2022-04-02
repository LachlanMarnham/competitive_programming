import pytest

from .solution import index_power


def checkio_main(array, n, solution):
    assert index_power(array, n) == solution


@pytest.mark.parametrize('array, n, solution', [
    ([1, 2, 3, 4], 2, 9),
    ([1, 3, 10, 100], 3, 1000000),
    ([0, 1], 0, 1),
    ([1, 2], 3, -1),
])
def test(array, n, solution):
    checkio_main(array, n, solution)
