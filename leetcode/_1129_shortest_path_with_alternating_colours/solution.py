from collections import defaultdict, deque
from dataclasses import dataclass
from typing import List


@dataclass
class QueueItem:
    node: int
    distance: int
    previous_colour: str


class Graph:
    def __init__(self):
        self._blue_edges = defaultdict(list)
        self._red_edges = defaultdict(list)

    def add_edge(self, colour: str, start: int, end: int) -> None:
        if colour == "blue":
            self._blue_edges[start].append(end)
        elif colour == "red":
            self._red_edges[start].append(end)

    @classmethod
    def from_edges(cls, red_edges: List[List[int]], blue_edges: List[List[int]]) -> "Graph":
        self = cls()
        for start, end in red_edges:
            self.add_edge("red", start, end)
        for start, end in blue_edges:
            self.add_edge("blue", start, end)
        return self

    def bfs(self, start: int, end: int) -> int:
        red_visited = set()
        blue_visited = set()
        queue = deque()
        for neighbour in self._blue_edges[start]:
            item = QueueItem(node=neighbour, distance=1, previous_colour="blue")
            blue_visited.add(neighbour)
            queue.append(item)
        for neighbour in self._red_edges[start]:
            item = QueueItem(node=neighbour, distance=1, previous_colour="red")
            red_visited.add(neighbour)
            queue.append(item)
        while queue:
            item = queue.popleft()
            if item.node == end:
                return item.distance
            elif item.previous_colour == "red":
                for neighbour in self._blue_edges[item.node]:
                    if neighbour not in blue_visited:
                        next_item = QueueItem(node=neighbour, distance=item.distance + 1, previous_colour="blue")
                        queue.append(next_item)
                        blue_visited.add(neighbour)
            elif item.previous_colour == "blue":
                for neighbour in self._red_edges[item.node]:
                    if neighbour not in red_visited:
                        next_item = QueueItem(node=neighbour, distance=item.distance + 1, previous_colour="red")
                        queue.append(next_item)
                        red_visited.add(neighbour)
        return -1


class Solution:
    def shortest_alternating_paths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph = Graph.from_edges(red_edges, blue_edges)
        answers = [0] * n
        for end in range(1, n):
            answer = graph.bfs(0, end)
            answers[end] = answer
        return answers
