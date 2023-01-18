import pytest

from .solution import pairs


def hackerrank_main(test_case):
    input_lines = test_case.strip().splitlines()
    _, k = tuple(map(int, input_lines.pop(0).rstrip().split()))

    arr = list(map(int, input_lines.pop(0).rstrip().split()))

    return pairs(k, arr)


TEST_CASE_15 = """5 2
1 5 3 4 2"""

TEST_CASE_16 = """10 1
363374326 364147530 61825163 1073065718 1281246024 1399469912 428047635 491595254 879792181 1069262793"""

TEST_CASE_17 = """7 2
1 3 5 8 6 4 2"""


@pytest.mark.parametrize(
    "test_case, solution",
    (
        (TEST_CASE_15, 3),
        (TEST_CASE_16, 0),
        (TEST_CASE_17, 5),
    ),
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
