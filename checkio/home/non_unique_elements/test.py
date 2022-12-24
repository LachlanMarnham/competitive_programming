import pytest

from .solution import non_unique_elements


def checkio_main(data, solution):
    assert non_unique_elements(data) == solution


@pytest.mark.parametrize(
    "data, solution",
    [
        ([1, 2, 3, 1, 3], [1, 3, 1, 3]),
        ([1, 2, 3, 4, 5], []),
        ([5, 5, 5, 5, 5], [5, 5, 5, 5, 5]),
        ([10, 9, 10, 10, 9, 8], [10, 9, 10, 10, 9]),
    ],
)
def test(data, solution):
    checkio_main(data, solution)
