import pytest

from .solution import replace_first


def checkio_main(items, solution):
    assert replace_first(items) == solution


@pytest.mark.parametrize('items, solution', [
    ([1, 2, 3, 4], [2, 3, 4, 1]),
    ([1], [1]),
    ([], []),
])
def test(items, solution):
    checkio_main(items, solution)
