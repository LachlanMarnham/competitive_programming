import pytest

from .solution import BinarySearchTree, lca


def hackerrank_main(test_case):
    input_lines = test_case.splitlines()

    tree = BinarySearchTree()
    num_nodes = int(input_lines.pop(0))

    arr = list(map(int, input_lines.pop(0).split()))

    for i in range(num_nodes):
        tree.create(arr[i])

    v = list(map(int, input_lines.pop(0).split()))

    ans = lca(tree.root, v[0], v[1])
    return ans.info


TEST_CASE_0 = """6
4 2 3 1 7 6
1 7"""

TEST_CASE_5 = """2
1 2
1 2"""

TEST_CASE_9 = """7
5 3 8 2 4 6 7
7 3"""


@pytest.mark.parametrize(
    "test_case, solution",
    [
        (TEST_CASE_0, 4),
        (TEST_CASE_5, 1),
        (TEST_CASE_9, 5),
    ],
)
def test(test_case, solution):
    assert hackerrank_main(test_case) == solution
