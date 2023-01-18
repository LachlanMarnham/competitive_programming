import pytest

from .solution import sum_numbers


def checkio_main(text, solution):
    assert sum_numbers(text) == solution


@pytest.mark.parametrize(
    "text, solution",
    [
        (
            "This picture is an oil on canvas " "painting by Danish artist Anna " "Petersen between 1845 and 1910 year",
            3755,
        ),
        ("hi", 0),
        ("who is 1st here", 0),
        ("my numbers is 2", 2),
        ("5 plus 6 is", 11),
        ("", 0),
    ],
)
def test(text, solution):
    checkio_main(text, solution)
