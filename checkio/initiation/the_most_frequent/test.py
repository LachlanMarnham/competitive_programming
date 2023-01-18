import pytest

from .solution import most_frequent


def checkio_main(data, solution):
    assert most_frequent(data) == solution


@pytest.mark.parametrize(
    "data, solution",
    [
        (["a", "b", "c", "a", "b", "a"], "a"),
        (["a", "a", "bi", "bi", "bi"], "bi"),
    ],
)
def test(data, solution):
    checkio_main(data, solution)
