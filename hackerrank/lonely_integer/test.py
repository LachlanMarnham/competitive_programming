import pytest

from .solution import lonely_integer


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()

    _ = int(input_lines.pop(0).strip())

    arr = list(map(int, input_lines.pop(0).rstrip().split()))

    return lonely_integer(arr)


TEST_CASE_0 = """1
1"""

TEST_CASE_1 = """3
1 1 2"""

TEST_CASE_2 = """5
0 0 1 2 1"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_0, 1),
        (TEST_CASE_1, 2),
        (TEST_CASE_2, 2),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
