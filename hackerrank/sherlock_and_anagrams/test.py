import pytest

from .solution import sherlock_and_anagrams


def hackerrank_main(test_case):
    results = []
    input_lines = test_case.splitlines()
    q = int(input_lines.pop(0).strip())
    for _ in range(q):
        s = input_lines.pop(0)
        result = sherlock_and_anagrams(s)
        results.append(result)

    return results


TEST_CASE_0 = """2
abba
abcd"""

TEST_CASE_1 = """2
ifailuhkqq
kkkk"""

TEST_CASE_6 = """1
cdcd"""


@pytest.mark.parametrize('test_case, solution', [
    (TEST_CASE_0, [4, 0]),
    (TEST_CASE_1, [3, 10]),
    (TEST_CASE_6, [5]),
])
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
