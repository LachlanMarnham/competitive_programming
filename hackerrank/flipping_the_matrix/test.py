import pytest

from .solution import flipping_matrix


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    q = int(input_lines.pop(0).strip())

    for _ in range(q):
        n = int(input_lines.pop(0).strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input_lines.pop(0).rstrip().split())))

        return flipping_matrix(matrix)


TEST_CASE_0 = """1
2
112 42 83 119
56 125 56 49
15 78 101 43
62 98 114 108"""

TEST_CASE_7 = """1
2
107 54 128 15
12 75 110 138
100 96 34 85
75 15 28 112"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_0, 414),
        (TEST_CASE_7, 488),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
