import pytest

from .solution import minimum_absolute_difference


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    _ = int(input_lines.pop(0).strip())

    arr = list(map(int, input_lines.pop(0).rstrip().split()))

    return minimum_absolute_difference(arr)


TEST_CASE_0 = """3
3 -7 0"""

TEST_CASE_1 = """10
-59 -36 -13 1 -53 -92 -2 -96 -54 75"""

TEST_CASE_10 = """5
1 -3 71 68 17"""


@pytest.mark.parametrize('test_case, solution', [
    (TEST_CASE_0, 3),
    (TEST_CASE_1, 1),
    (TEST_CASE_10, 3),
])
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
