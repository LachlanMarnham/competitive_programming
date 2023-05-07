import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "s, k, result",
    (("abciiidef", 3, 3), ("aeiou", 2, 2), ("leetcode", 3, 2)),
)
def test(s, k, result):
    tester = Solution()
    assert tester.max_vowels(s, k) == result
