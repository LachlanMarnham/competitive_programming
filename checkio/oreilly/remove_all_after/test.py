import pytest

from .solution import remove_all_after


def checkio_main(items, border, solution):
    assert remove_all_after(items, border) == solution


@pytest.mark.parametrize(
    "items, border, solution",
    [
        ([1, 2, 3, 4, 5], 3, [1, 2, 3]),
        ([1, 1, 2, 2, 3, 3], 2, [1, 1, 2]),
        ([1, 1, 2, 4, 2, 3, 4], 2, [1, 1, 2]),
        ([1, 1, 5, 6, 7], 2, [1, 1, 5, 6, 7]),
        ([], 0, []),
        ([7, 7, 7, 7, 7, 7, 7, 7, 7], 7, [7]),
    ],
)
def test(items, border, solution):
    checkio_main(items, border, solution)
