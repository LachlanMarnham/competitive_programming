import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "input, output",
    (
        ("III", 3),
        ("LVIII", 58),
        ("MCMXCIV", 1994),
    ),
)
def test(input, output):
    tester = Solution()
    assert tester.roman_to_int(input) == output
