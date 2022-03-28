import pytest

from .solution import check_magazine


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    _ = input_lines.pop(0).rstrip().split()

    magazine = input_lines.pop(0).rstrip().split()

    note = input_lines.pop(0).rstrip().split()

    return check_magazine(magazine, note)


TEST_CASE_0 = """6 4
give me one grand today night
give one grand today"""

TEST_CASE_20 = """6 5
two times three is not four
two times two is four"""

TEST_CASE_21 = """7 4
ive got a lovely bunch of coconuts
ive got some coconuts"""


@pytest.mark.parametrize('test_case, solution', [
    (TEST_CASE_0, 'Yes'),
    (TEST_CASE_20, 'No'),
    (TEST_CASE_21, 'No'),
])
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
