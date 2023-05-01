import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "nums, target, expected_output",
    (
        ([1, 3, 5, 6], 5, 2),
        ([1, 3, 5, 6], 2, 1),
        ([1, 3, 5, 6], 7, 4),
    ),
)
def test(nums, target, expected_output):
    tester = Solution()
    assert tester.search_insert(nums, target) == expected_output
