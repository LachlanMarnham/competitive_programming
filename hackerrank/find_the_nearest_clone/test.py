import pytest

from .solution import find_shortest


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()
    graph_nodes, graph_edges = map(int, input_lines.pop(0).split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input_lines.pop(0).split())

    ids = list(map(int, input_lines.pop(0).rstrip().split()))

    val = int(input_lines.pop(0))

    ans = find_shortest(graph_nodes, graph_from, graph_to, ids, val)
    return ans


TEST_CASE_0 = """4 3
1 2
1 3
4 2
1 2 1 1
1"""

TEST_CASE_1 = """4 3
1 2
1 3
4 2
1 2 3 4
2"""

TEST_CASE_12 = """5 4
1 2
1 3
2 4
3 5
1 2 3 3 2
2"""


@pytest.mark.parametrize('test_case, solution', [
    (TEST_CASE_0, 1),
    (TEST_CASE_1, -1),
    (TEST_CASE_12, 3),
])
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
