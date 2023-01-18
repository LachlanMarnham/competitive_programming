import pytest

from .solution import two_strings


def hackerrank_main(test_case):
    results = []
    input_lines = test_case.splitlines()
    q = int(input_lines.pop(0).strip())
    for _ in range(q):
        s1 = input_lines.pop(0)
        s2 = input_lines.pop(0)
        result = two_strings(s1, s2)
        results.append(result)

    return results


TEST_CASE_0 = """2
hello
world
hi
world"""

TEST_CASE_6 = """4
wouldyoulikefries
abcabcabcabcabcabc
hackerrankcommunity
cdecdecdecde
jackandjill
wentupthehill
writetoyourparents
fghmqzldbc"""

TEST_CASE_7 = """2
aardvark
apple
beetroot
sandals"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_0, ["YES", "NO"]),
        (TEST_CASE_6, ["NO", "YES", "YES", "NO"]),
        (TEST_CASE_7, ["YES", "NO"]),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
