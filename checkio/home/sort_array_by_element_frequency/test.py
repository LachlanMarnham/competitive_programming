import pytest

from .solution import frequency_sort


def checkio_main(items, solution):
    assert frequency_sort(items) == solution


@pytest.mark.parametrize('items, solution', [
    ([4, 6, 2, 2, 6, 4, 4, 4], [4, 4, 4, 4, 6, 6, 2, 2]),
    (['bob', 'bob', 'carl', 'alex', 'bob'], ['bob', 'bob', 'bob', 'carl', 'alex']),
    ([17, 99, 42], [17, 99, 42]),
    ([], []),
    ([1], [1]),
])
def test(items, solution):
    checkio_main(items, solution)
