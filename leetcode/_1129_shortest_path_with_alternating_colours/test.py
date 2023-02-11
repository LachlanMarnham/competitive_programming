import pytest

from .solution import Solution


@pytest.mark.parametrize(
    "n, red_edges, blue_edges, answer",
    (
        (3, [[0, 1], [1, 2]], [], [0, 1, -1]),
        (3, [[0, 1]], [[2, 1]], [0, 1, -1]),
    ),
)
def test(n, red_edges, blue_edges, answer):
    assert Solution().shortest_alternating_paths(n, red_edges, blue_edges) == answer
