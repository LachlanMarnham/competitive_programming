import pytest

from .solution import super_digit


def hackerrank_main(test_case):
    n, k = test_case.split()

    return super_digit(n, k)


TEST_CASE_0 = """148 3"""

TEST_CASE_10 = """9875 4"""

TEST_CASE_11 = """123 3"""


@pytest.mark.parametrize(
    "test_case, solution",
    (
        (TEST_CASE_0, 3),
        (TEST_CASE_10, 8),
        (TEST_CASE_11, 9),
    ),
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
