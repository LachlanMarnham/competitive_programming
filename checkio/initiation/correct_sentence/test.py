import pytest

from .solution import correct_sentence


def checkio_main(text, solution):
    assert correct_sentence(text) == solution


@pytest.mark.parametrize(
    "text, solution",
    [
        ("greetings, friends", "Greetings, friends."),
        ("Greetings, friends", "Greetings, friends."),
        ("Greetings, friends.", "Greetings, friends."),
        ("hi", "Hi."),
        ("welcome to New York", "Welcome to New York."),
    ],
)
def test(text, solution):
    checkio_main(text, solution)
