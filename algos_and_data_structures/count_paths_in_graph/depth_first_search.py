from collections import defaultdict
from typing import Set


class Counter:
    """We need to count the number of paths, and to do that we want to
    pass something down the recursion stack. However count += 1  type stuff
    wont work because ints are immutable. `Counter` just functions as a
    muteable int"""

    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


class Graph:
    def __init__(self, num_nodes: int) -> None:
        self.num_nodes = num_nodes
        self.neighbours = defaultdict(list)

    def add_edge(self, start: int, end: int) -> None:
        """This assumes the edges are directed. For an undirected
        graph, we would also want self.neighbours[end].append(start)"""
        self.neighbours[start].append(end)

    def dfs(self, start: int, end: int, visited: Set[int], num_paths: Counter):
        visited.add(start)
        for neighbour in self.neighbours[start]:
            if neighbour == end:
                num_paths.increment()
            elif neighbour not in visited:
                self.dfs(neighbour, end, visited, num_paths)
        visited.remove(start)
        return

    def count_paths(self, start: int, end: int) -> int:
        visited = set()
        num_paths = Counter()
        self.dfs(start, end, visited, num_paths)
        return num_paths.count
