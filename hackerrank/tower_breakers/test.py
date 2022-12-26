import pytest

from .solution import tower_breakers


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    t = int(input_lines.pop(0).strip())
    results = []
    for t_itr in range(t):
        first_multiple_input = input_lines.pop(0).rstrip().split()
        n = int(first_multiple_input[0])
        m = int(first_multiple_input[1])
        result = tower_breakers(n, m)
        results.append(result)
    return results


TEST_CASE_0 = """2
2 2
1 4"""

TEST_CASE_1 = """2
1 7
3 7"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_0, [2, 1]),
        (TEST_CASE_1, [1, 1]),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
