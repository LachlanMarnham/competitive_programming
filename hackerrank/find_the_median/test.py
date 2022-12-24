import pytest

from .solution import find_median


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    arr = list(map(int, input_lines.pop().rstrip().split()))

    return find_median(arr)


TEST_CASE_0 = """7
0 1 2 4 6 5 3"""


def test():
    assert hackerrank_main(TEST_CASE_0) == 3
