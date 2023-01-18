import pytest

from .solution import maximum_toys


def hackerrank_main(test_case):
    input_lines = test_case.strip().splitlines()
    _, k = input_lines.pop(0).rstrip().split()

    prices = list(map(int, input_lines.pop(0).rstrip().split()))

    return maximum_toys(prices, int(k))


TEST_CASE_0 = """7 50
1 12 5 111 200 1000 10"""

TEST_CASE_16 = """4 7
1 2 3 4"""

TEST_CASE_17 = """5 15
3 7 2 9 4"""


@pytest.mark.parametrize(
    "test_case, solution",
    (
        (TEST_CASE_0, 4),
        (TEST_CASE_16, 3),
        (TEST_CASE_17, 3),
    ),
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
