import pytest

from .solution import split_list


def checkio_main(items, solution):
    assert split_list(items) == solution


@pytest.mark.parametrize(
    "items, solution",
    [
        ([1, 2, 3, 4, 5, 6], [[1, 2, 3], [4, 5, 6]]),
        ([1, 2, 3], [[1, 2], [3]]),
        ([1, 2, 3, 4, 5], [[1, 2, 3], [4, 5]]),
        ([1], [[1], []]),
        ([], [[], []]),
    ],
)
def test(items, solution):
    checkio_main(items, solution)
