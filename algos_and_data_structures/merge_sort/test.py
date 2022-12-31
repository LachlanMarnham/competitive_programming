import random

import pytest

from .merge_sort import merge_sort


@pytest.mark.parametrize(
    "input, output",
    (
        ([1, 2, 3], [1, 2, 3]),
        ([3, 2, 1], [1, 2, 3]),
        ([1, 1, 1], [1, 1, 1]),
    ),
)
def test(input, output):
    assert merge_sort(input) == output


def test_long():
    arr = [random.randint(0, 100) for _ in range(100)]
    expected_result = sorted(arr.copy())
    assert merge_sort(arr) == expected_result
