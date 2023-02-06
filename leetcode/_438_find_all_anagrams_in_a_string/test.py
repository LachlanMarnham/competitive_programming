import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "s, p, output",
    (
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2]),
    ),
)
def test(s, p, output):
    tester = Solution()
    assert tester.find_anagrams(s, p) == output
