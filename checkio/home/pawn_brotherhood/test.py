import pytest

from .solution import safe_pawns


def checkio_main(pawns, solution):
    assert safe_pawns(pawns) == solution


@pytest.mark.parametrize('pawns, solution', [
    ({'b4', 'd4', 'f4', 'c3', 'e3', 'g5', 'd2'}, 6),
    ({'b4', 'c4', 'd4', 'e4', 'f4', 'g4', 'e5'}, 1),
])
def test(pawns, solution):
    checkio_main(pawns, solution)
