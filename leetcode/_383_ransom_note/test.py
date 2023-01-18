import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "ransom_note, magazine, output",
    (
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
    ),
)
def test(ransom_note, magazine, output):
    tester = Solution()
    assert tester.can_construct(ransom_note, magazine) == output
