import pytest

from .solution import luck_balance


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()

    first_multiple_input = input_lines.pop(0).rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input_lines.pop(0).rstrip().split())))

    return luck_balance(k, contests)


TEST_CASE_0 = """6 3
5 1
2 1
1 1
8 1
10 0
5 0"""

TEST_CASE_3 = """8 5
13 1
10 1
9 1
8 1
13 1
12 1
18 1
13 1"""

TEST_CASE_12 = """5 2
5 1
4 0
6 1
2 1
8 0"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_0, 29),
        (TEST_CASE_3, 42),
        (TEST_CASE_12, 21),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
