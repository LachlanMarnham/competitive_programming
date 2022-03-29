import pytest

from .solution import end_zeros


def checkio_main(num, solution):
    assert end_zeros(num) == solution


@pytest.mark.parametrize('num, solution', [
    (0, 1),
    (1, 0),
    (10, 1),
    (101, 0),
    (245, 0),
    (100100, 2),
])
def test(num, solution):
    checkio_main(num, solution)
