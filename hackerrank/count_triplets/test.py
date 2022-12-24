import pytest

from .solution import count_triplets


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    nr = input_lines.pop(0).split()
    r = int(nr[1])
    arr = list(map(int, input_lines.pop(0).rstrip().split()))
    return count_triplets(arr, r)


TEST_CASE_0 = """4 2
1 2 2 4"""

TEST_CASE_1 = """6 3
1 3 9 9 27 81"""

TEST_CASE_12 = """5 5
1 5 5 25 125"""


@pytest.mark.parametrize('test_case, solution', [
    (TEST_CASE_0, 2),
    (TEST_CASE_1, 6),
    (TEST_CASE_12, 4),
])
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
