import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "nums_1, nums_2, output",
    (
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
    ),
)
def test(nums_1, nums_2, output):
    solver = Solution()
    assert solver.find_median_sorted_arrays(nums_1, nums_2) == output
