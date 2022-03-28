import pytest

from .solution import hourglass_sum


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input_lines.pop(0).rstrip().split())))

    return hourglass_sum(arr)


TEST_CASE_0 = """1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0"""

TEST_CASE_1 = """1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 9 2 -4 -4 0
0 0 0 -2 0 0
0 0 -1 -2 -4 0"""

TEST_CASE_8 = """-9 -9 -9 1 1 1
0 -9 0 4 3 2
-9 -9 -9 1 2 3
0 0 8 6 6 0
0 0 0 -2 0 0
0 0 1 2 4 0"""


@pytest.mark.parametrize('test_case, solution', [
    (TEST_CASE_0, 19),
    (TEST_CASE_1, 13),
    (TEST_CASE_8, 28),
])
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
