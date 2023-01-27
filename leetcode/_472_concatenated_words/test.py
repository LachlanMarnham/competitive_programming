import pytest

from .solution import Solution


@pytest.mark.parametrize('words, output', (
    (["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"], ["catsdogcats","dogcatsdog","ratcatdogcat"]),
    (["cat","dog","catdog"], ["catdog"]),
))
def test(words, output):
    tester = Solution()
    assert set(tester.find_concatenated_words(words)) == set(output)
