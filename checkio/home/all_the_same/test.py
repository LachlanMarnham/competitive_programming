import pytest

from .solution import all_the_same


def checkio_main(elements, solution):
    assert all_the_same(elements) == solution


@pytest.mark.parametrize(
    "elements, solution",
    [
        ([1, 1, 1], True),
        ([1, 2, 1], False),
        (["a", "a", "a"], True),
        ([], True),
        ([1], True),
    ],
)
def test(elements, solution):
    checkio_main(elements, solution)
