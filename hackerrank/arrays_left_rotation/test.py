import pytest

from .solution import rotLeft


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    first_multiple_input = input_lines.pop(0).rstrip().split()
    _ = int(first_multiple_input[0])
    num_rotations = int(first_multiple_input[1])
    arr = list(map(int, input_lines.pop(0).rstrip().split()))
    return rotLeft(arr, num_rotations)


TEST_CASE_0 = """5 4
1 2 3 4 5"""

TEST_CASE_1 = """20 10
41 73 89 7 10 1 59 58 84 77 77 97 58 1 86 58 26 10 86 51"""

TEST_CASE_10 = """15 13
33 47 70 37 8 53 13 93 71 72 51 100 60 87 97"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_0, [5, 1, 2, 3, 4]),
        (TEST_CASE_1, [77, 97, 58, 1, 86, 58, 26, 10, 86, 51, 41, 73, 89, 7, 10, 1, 59, 58, 84, 77]),
        (TEST_CASE_10, [87, 97, 33, 47, 70, 37, 8, 53, 13, 93, 71, 72, 51, 100, 60]),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
