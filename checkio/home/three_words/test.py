import pytest

from .solution import three_words


def checkio_main(words, solution):
    assert three_words(words) == solution


@pytest.mark.parametrize(
    "words, solution",
    [
        ("Hello World hello", True),
        ("He is 123 man", False),
        ("1 2 3 4", False),
        ("bla bla bla bla", True),
        ("Hi", False),
    ],
)
def test(words, solution):
    checkio_main(words, solution)
