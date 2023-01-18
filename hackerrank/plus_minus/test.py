import pytest

from .solution import plus_minus


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    _ = int(input_lines.pop(0).strip())
    arr = list(map(int, input_lines.pop(0).rstrip().split()))
    return plus_minus(arr)


TEST_CASE_1 = """6
-4 3 -9 0 4 1"""

TEST_CASE_11 = """8
1 2 3 -1 -2 -3 0 0"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_1, ["0.500000", "0.333333", "0.166667"]),
        (TEST_CASE_11, ["0.375000", "0.375000", "0.250000"]),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
