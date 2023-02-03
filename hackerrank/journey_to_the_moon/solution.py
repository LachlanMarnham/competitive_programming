import os
from collections import defaultdict, deque
from typing import List, Set


class Graph:
    def __init__(self, num_nodes: int) -> None:
        self._neighbours = defaultdict(set)
        self._num_nodes = num_nodes

    def _add_edge(self, astronaut_1: int, astronaut_2: int) -> None:
        self._neighbours[astronaut_1].add(astronaut_2)
        self._neighbours[astronaut_2].add(astronaut_1)

    @classmethod
    def from_pairs(cls, num_nodes: int, astronaut_pairs: List[List[int]]) -> "Graph":
        self = cls(num_nodes)
        for astronaut_1, astronaut_2 in astronaut_pairs:
            self._add_edge(astronaut_1, astronaut_2)
        return self

    def _get_subgraph_size(self, start: int, visited: Set[int]) -> int:
        queue = deque()
        queue.appendleft(start)
        visited.add(start)
        size = 1
        while queue:
            next_node = queue.pop()
            neighbours = self._neighbours[next_node]
            for neighbour in neighbours:
                if neighbour not in visited:
                    queue.appendleft(neighbour)
                    visited.add(neighbour)
                    size += 1
        return size

    def _count_pairs_from_subgraph_sizes(self, subgraph_sizes: List[int]) -> int:
        """The number of possible pairs is the product of subgraph sizes.
        Ie, if we have three subraphs of sizes (a, b, c), the result is
            ab + ac + bc
        Note, however that
            (a + b + c)^2 = a^2 + b^2 + c^2 + 2ab + 2ac + 2bc
        So we can rewrite
            ab + ac + bc = [(a + b + c)^2 - a^2 - b^2 - c^2] / 2
        This is true in general for an arbitrary number of subraphs,
        but it's tricky to write the proof in a docstring...
        Anyway, using this identity allows us to calculate the result
        in O(n) instead of O(n^2)"""
        square_of_sum = sum(subgraph_sizes) ** 2
        sum_of_squares = sum(map(lambda n: n**2, subgraph_sizes))
        return (square_of_sum - sum_of_squares) // 2

    def count_pairs(self) -> int:
        visited = set()
        subgraph_sizes = []
        for start in range(self._num_nodes):
            if start not in visited:
                size = self._get_subgraph_size(start, visited)
                subgraph_sizes.append(size)
        return self._count_pairs_from_subgraph_sizes(subgraph_sizes)


def journey_to_moon(num_astronauts: int, astronaut_pairs: List[List[int]]):
    graph = Graph.from_pairs(num_astronauts, astronaut_pairs)
    return graph.count_pairs()
