import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "s1, s2, output",
    (
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
    ),
)
def test(s1, s2, output):
    tester = Solution()
    assert tester.check_inclusion(s1, s2) == output
