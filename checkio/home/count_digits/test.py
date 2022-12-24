import pytest

from .solution import count_digits


def checkio_main(text, solution):
    assert count_digits(text) == solution


@pytest.mark.parametrize(
    "text, solution",
    [
        ("hi", 0),
        ("who is 1st here", 1),
        ("my numbers is 2", 1),
        (
            "This picture is an oil on canvas " "painting by Danish artist Anna " "1845 and 1910 year",
            8,
        ),
        ("5 plus 6 is", 2),
        ("", 0),
    ],
)
def test(text, solution):
    checkio_main(text, solution)
