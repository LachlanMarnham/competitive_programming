import pytest

from .solution import jumping_on_clouds


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    _ = int(input_lines.pop(0).strip())
    c = list(map(int, input_lines.pop(0).rstrip().split()))
    return jumping_on_clouds(c)


TEST_CASE_0 = """7
0 0 1 0 0 1 0"""

TEST_CASE_1 = """6
0 0 0 1 0 0"""


@pytest.mark.parametrize('test_case, solution', [
    (TEST_CASE_0, 4),
    (TEST_CASE_1, 3),
])
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
