from .solution import findShortest
import pytest

def hackerrank_main(test_case):
    inputs = test_case.splitlines()
    graph_nodes, graph_edges = map(int, inputs.pop(0).split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, inputs.pop(0).split())

    ids = list(map(int, inputs.pop(0).rstrip().split()))

    val = int(inputs.pop(0))

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)
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

@pytest.mark.parametrize('test_case, solution', [
    (TEST_CASE_0, 1),
    (TEST_CASE_1, -1),
])
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
