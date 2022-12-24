import pytest

from .solution import mini_max_sum


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    arr = list(map(int, input_lines.pop(0).rstrip().split()))

    return mini_max_sum(arr)


TEST_CASE_1 = """1 2 3 4 5"""

TEST_CASE_14 = """7 69 2 221 8974"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_1, [10, 14]),
        (TEST_CASE_14, [299, 9271]),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
