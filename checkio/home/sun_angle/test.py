import pytest

from .solution import sun_angle


def checkio_main(time, solution):
    assert sun_angle(time) == solution


@pytest.mark.parametrize(
    "time, solution",
    [
        ("07:00", 15),
        ("01:23", "I don't see the sun!"),
    ],
)
def test(time, solution):
    checkio_main(time, solution)
