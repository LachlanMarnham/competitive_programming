import pytest

from .solution import arrayManipulation


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()

    first_multiple_input = input_lines.pop(0).rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])

    queries = []
    for _ in range(m):
        queries.append(list(map(int, input_lines.pop(0).rstrip().split())))

    return arrayManipulation(n, queries)


TEST_CASE_0 = """5 3
1 2 100
2 5 100
3 4 100"""

TEST_CASE_14 = """10 3
1 5 3
4 8 7
6 9 1"""

TEST_CASE_15 = """10 4
2 6 8
3 5 7
1 8 1
5 9 15"""


@pytest.mark.parametrize('test_case, solution', [
    (TEST_CASE_0, 200),
    (TEST_CASE_14, 10),
    (TEST_CASE_15, 31),
])
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
