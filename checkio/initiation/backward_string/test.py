import pytest

from .solution import backward_string


def checkio_main(val, solution):
    assert backward_string(val) == solution


@pytest.mark.parametrize(
    "val, solution",
    [
        ("val", "lav"),
        ("", ""),
        ("ohho", "ohho"),
        ("123456789", "987654321"),
    ],
)
def test(val, solution):
    checkio_main(val, solution)
