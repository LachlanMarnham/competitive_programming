import pytest

from .solution import split_pairs


def checkio_main(a, solution):
    assert split_pairs(a) == solution


@pytest.mark.parametrize('a, solution', [
    ('abcd', ['ab', 'cd']),
    ('abc', ['ab', 'c_']),
    ('abcdf', ['ab', 'cd', 'f_']),
    ('a', ['a_']),
    ('', []),
])
def test(a, solution):
    checkio_main(a, solution)
