import pytest

from .solution import is_acceptable_password


def checkio_main(password, solution):
    assert is_acceptable_password(password) == solution


@pytest.mark.parametrize(
    "password, solution",
    [
        ("short", False),
        ("muchlonger", True),
        ("ashort", False),
    ],
)
def test(password, solution):
    checkio_main(password, solution)
