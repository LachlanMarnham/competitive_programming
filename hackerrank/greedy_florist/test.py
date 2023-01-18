import pytest

from .solution import get_minimum_cost


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()

    nk = input_lines.pop(0).split()

    num_friends = int(nk[1])

    flower_costs = list(map(int, input_lines.pop(0).rstrip().split()))

    return get_minimum_cost(num_friends, flower_costs)


TEST_CASE_0 = """3 3
2 5 6"""

TEST_CASE_10 = """3 2
2 5 6"""

TEST_CASE_11 = """5 3
1 3 5 7 9"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_0, 13),
        (TEST_CASE_10, 15),
        (TEST_CASE_11, 29),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
