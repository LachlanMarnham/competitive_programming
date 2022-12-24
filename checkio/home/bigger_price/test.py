import pytest

from .solution import bigger_price


def checkio_main(limit, data, solution):
    assert bigger_price(limit, data) == solution


@pytest.mark.parametrize(
    "limit, data, solution",
    [
        (
            2,
            [
                {"name": "bread", "price": 100},
                {"name": "wine", "price": 138},
                {"name": "meat", "price": 15},
                {"name": "water", "price": 1},
            ],
            [
                {"name": "wine", "price": 138},
                {"name": "bread", "price": 100},
            ],
        ),
        (
            1,
            [
                {"name": "pen", "price": 5},
                {"name": "whiteboard", "price": 170},
            ],
            [
                {"name": "whiteboard", "price": 170},
            ],
        ),
    ],
)
def test(limit, data, solution):
    checkio_main(limit, data, solution)
