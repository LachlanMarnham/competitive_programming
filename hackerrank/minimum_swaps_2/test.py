import pytest

from .solution import minimum_swaps


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    _ = int(input_lines.pop(0))
    arr = list(map(int, input_lines.pop(0).rstrip().split()))
    return minimum_swaps(arr)


TEST_CASE_0 = """4
4 3 1 2"""

TEST_CASE_1 = """5
2 3 4 1 5"""

TEST_CASE_2 = """7
1 3 5 2 4 6 7"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_0, 3),
        (TEST_CASE_1, 3),
        (TEST_CASE_2, 3),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
