import pytest

from .solution import count_swaps


def hackerrank_main(test_case):
    input_lines = test_case.strip().splitlines()
    _ = int(input_lines.pop(0).strip())
    arr = list(map(int, input_lines.pop(0).rstrip().split()))
    return count_swaps(arr)


TEST_CASE_0 = """3
1 2 3"""

TEST_CASE_1 = """3
3 2 1"""

TEST_CASE_3 = """4
4 2 3 1"""


@pytest.mark.parametrize(
    "test_case, solution",
    (
        (TEST_CASE_0, (0, 1, 3)),
        (TEST_CASE_1, (3, 1, 3)),
        (TEST_CASE_3, (5, 1, 4)),
    ),
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
