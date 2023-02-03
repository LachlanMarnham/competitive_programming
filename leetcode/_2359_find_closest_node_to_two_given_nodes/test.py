import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "edges, node_1, node_2, output",
    (
        ([2, 2, 3, -1], 0, 1, 2),
        ([1, 2, -1], 0, 2, 2),
    ),
)
def test(edges, node_1, node_2, output):
    solver = Solution()
    assert solver.closest_meeting_node(edges, node_1, node_2) == output
