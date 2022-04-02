import pytest

from .solution import replace_last


def checkio_main(line, solution):
    assert replace_last(line) == solution


@pytest.mark.parametrize('line, solution', [
    ([2, 3, 4, 1], [1, 2, 3, 4]),
    ([1, 2, 3, 4], [4, 1, 2, 3]),
    ([1], [1]),
    ([], []),
])
def test(line, solution):
    checkio_main(line, solution)
