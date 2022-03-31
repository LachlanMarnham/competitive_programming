import pytest

from .solution import second_index


def checkio_main(text, symbol, solution):
    assert second_index(text, symbol) == solution


@pytest.mark.parametrize('text, symbol, solution', [
    ('sims', 's', 3),
    ('find the river', 'e', 12),
    ('hi', ' ', None),
    ('hi mayor', ' ', None),
    ('hi mr Mayor', ' ', 5),
])
def test(text, symbol, solution):
    checkio_main(text, symbol, solution)
