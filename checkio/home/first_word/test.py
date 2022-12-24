import pytest

from .solution import first_word


def checkio_main(text, solution):
    assert first_word(text) == solution


@pytest.mark.parametrize(
    "text, solution",
    [
        ("Hello world", "Hello"),
        (" a word ", "a"),
        ("don't touch it", "don't"),
        ("greetings, friends", "greetings"),
        ("... and so on ...", "and"),
        ("hi", "hi"),
        ("Hello.World", "Hello"),
    ],
)
def test(text, solution):
    checkio_main(text, solution)
