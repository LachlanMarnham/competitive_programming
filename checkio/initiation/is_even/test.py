import pytest

from .solution import is_even


def checkio_main(num, solution):
    assert is_even(num) == solution


@pytest.mark.parametrize('num, solution', [
    (2, True),
    (5, False),
    (0, True),
])
def test(num, solution):
    checkio_main(num, solution)
