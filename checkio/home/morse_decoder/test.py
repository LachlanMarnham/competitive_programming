import pytest

from .solution import morse_decoder


def checkio_main(code, solution):
    assert morse_decoder(code) == solution


@pytest.mark.parametrize(
    "code, solution",
    [
        (
            "... --- -- .   - . -..- -",
            "Some text",
        ),
        (
            "..--- ----- .---- ---..",
            "2018",
        ),
        (
            ".. -   .-- .- ...   .-   --. --- --- -..   -.. .- -.--",
            "It was a good day",
        ),
    ],
)
def test(code, solution):
    checkio_main(code, solution)
