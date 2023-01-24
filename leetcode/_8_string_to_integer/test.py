import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "input, output",
    (
        ("   -42", -42),
        ("42", 42),
        ("4193 with words", 4193),
    ),
)
def test(input, output):
    tester = Solution()
    assert tester.my_atoi(input) == output
