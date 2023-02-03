import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "words, order, output",
    (
        (["hello", "leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
        (["word", "world", "row"], "worldabcefghijkmnpqstuvxyz", False),
        (["apple", "app"], "abcdefghijklmnopqrstuvwxyz", False),
    ),
)
def test(words, order, output):
    tester = Solution()
    assert tester.is_alien_sorted(words, order) is output
