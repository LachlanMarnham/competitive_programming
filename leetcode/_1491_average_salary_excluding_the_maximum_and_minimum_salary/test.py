import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "salary, output",
    (
        ([4000, 3000, 1000, 2000], 2500.0),
        ([1000, 2000, 3000], 2000.0),
    ),
)
def test(salary, output):
    tester = Solution()
    assert tester.average(salary) == output
