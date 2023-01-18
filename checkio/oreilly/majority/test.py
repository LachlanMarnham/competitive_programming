import pytest

from .solution import is_majority


def checkio_main(items, solution):
    assert is_majority(items) == solution


@pytest.mark.parametrize(
    "items, solution",
    [
        ([True, True, False, True, False], True),
        ([True, True, False], True),
        ([True, True, False, False], False),
        ([True, True, False, False, False], False),
        ([False], False),
        ([True], True),
        ([], False),
    ],
)
def test(items, solution):
    checkio_main(items, solution)
