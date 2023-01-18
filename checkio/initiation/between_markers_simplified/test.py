import pytest

from .solution import between_markers


def checkio_main(text, begin, end, solution):
    assert between_markers(text, begin, end) == solution


@pytest.mark.parametrize(
    "text, begin, end, solution",
    [
        ("What is >apple<", ">", "<", "apple"),
        ("What is [apple]", "[", "]", "apple"),
        ("What is ><", ">", "<", ""),
        (">apple<", ">", "<", "apple"),
    ],
)
def test(text, begin, end, solution):
    checkio_main(text, begin, end, solution)
