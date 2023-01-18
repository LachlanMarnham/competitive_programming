import pytest

from .solution import freq_query


def hackerrank_main(test_case):
    input_lines = test_case.strip().splitlines()
    num_queries = int(input_lines.pop(0).strip())

    queries = []

    for _ in range(num_queries):
        queries.append(list(map(int, input_lines.pop(0).strip().split())))

    return freq_query(queries)


TEST_CASE_0 = """8
1 5
1 6
3 2
1 10
1 10
1 6
2 5
3 2"""

TEST_CASE_1 = """4
3 4
2 1003
1 16
3 1"""

TEST_CASE_2 = """10
1 3
2 3
3 2
1 4
1 5
1 5
1 4
3 2
2 4
3 2"""


@pytest.mark.parametrize(
    "test_case, solution",
    (
        (TEST_CASE_0, [0, 1]),
        (TEST_CASE_1, [0, 1]),
        (TEST_CASE_2, [0, 1, 1]),
    ),
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
