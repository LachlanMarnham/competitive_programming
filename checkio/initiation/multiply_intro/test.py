import pytest

from .solution import mult_two


def checkio_main(a, b, solution):
    assert mult_two(a, b) == solution


@pytest.mark.parametrize('a, b, solution', [
    (3, 2, 6),
    (1, 0, 0),
])
def test(a, b, solution):
    checkio_main(a, b, solution)
