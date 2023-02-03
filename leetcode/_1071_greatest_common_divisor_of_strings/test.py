import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "str_1, str_2, output",
    (
        ("ABCABC", "ABC", "ABC"),
        ("ABABAB", "ABAB", "AB"),
        ("LEET", "CODE", ""),
    ),
)
def test(str_1, str_2, output):
    tester = Solution()
    assert tester.gcd_of_strings(str_1, str_2) == output
