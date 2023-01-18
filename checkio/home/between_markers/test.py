import pytest

from .solution import between_markers


def checkio_main(text, begin, end, solution):
    assert between_markers(text, begin, end) == solution


@pytest.mark.parametrize(
    "text, begin, end, solution",
    [
        ("What is >apple<", ">", "<", "apple"),
        ("<head><title>My new site</title></head>", "<title>", "</title>", "My new site"),
        ("No[/b] hi", "[b]", "[/b]", "No"),
        ("No [b]hi", "[b]", "[/b]", "hi"),
        ("No hi", "[b]", "[/b]", "No hi"),
        ("No <hi>", ">", "<", ""),
    ],
)
def test(text, begin, end, solution):
    checkio_main(text, begin, end, solution)
