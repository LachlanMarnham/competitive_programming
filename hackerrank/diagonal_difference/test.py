import pytest

from .solution import diagonal_difference


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    n = int(input_lines.pop(0).strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input_lines.pop(0).rstrip().split())))

    return diagonal_difference(arr)


TEST_CASE_0 = """3
11 2 4
4 5 6
10 8 -12"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_0, 15),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
