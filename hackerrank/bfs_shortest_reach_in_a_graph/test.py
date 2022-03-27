import pytest

from .solution import Graph


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    answers = []

    t = int(input_lines.pop(0))
    for _ in range(t):
        n, m = [int(value) for value in input_lines.pop(0).split()]
        graph = Graph(n)
        for _ in range(m):
            x, y = [int(x) for x in input_lines.pop(0).split()]
            graph.connect(x - 1, y - 1)
        s = int(input_lines.pop(0))
        answer = graph.find_all_distances(s - 1)
        answers.append(answer)

    return answers


TEST_CASE_0 = """2
4 2
1 2
1 3
1
3 1
2 3
2"""

TEST_CASE_1 = """1
6 4
1 2
2 3
3 4
1 5
1"""

TEST_CASE_2 = """1
7 4
1 2
1 3
3 4
2 5
2"""


@pytest.mark.parametrize('test_case, solution', [
    (TEST_CASE_0, ['6 6 -1', '-1 6']),
    (TEST_CASE_1, ['6 12 18 6 -1']),
    (TEST_CASE_2, ['6 12 18 6 -1 -1']),
])
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
