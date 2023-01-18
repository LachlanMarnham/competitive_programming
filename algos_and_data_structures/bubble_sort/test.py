import random

import pytest

from .bubble_sort import bubble_sort


@pytest.mark.parametrize(
    "input, output",
    (
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 1], [1, 1, 1]),
    ),
)
def test(input, output):
    assert bubble_sort(input) == output


def test_long():
    arr = [random.randint(0, 100) for _ in range(100)]
    expected_result = sorted(arr.copy())
    assert bubble_sort(arr) == expected_result
