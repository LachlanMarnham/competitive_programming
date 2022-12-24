import pytest

from .solution import date_time


def checkio_main(time, solution):
    assert date_time(time) == solution


@pytest.mark.parametrize(
    "time, solution",
    [
        ("01.01.2000 00:00", "1 January 2000 year 0 hours 0 minutes"),
        ("09.05.1945 06:30", "9 May 1945 year 6 hours 30 minutes"),
        ("20.11.1990 03:55", "20 November 1990 year 3 hours 55 minutes"),
    ],
)
def test(time, solution):
    checkio_main(time, solution)
