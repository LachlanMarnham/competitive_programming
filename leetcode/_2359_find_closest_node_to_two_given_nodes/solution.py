from collections import defaultdict, deque
from dataclasses import dataclass
from typing import List


@dataclass
class QueueItem:
    node: int
    distance: int


class Graph:
    def __init__(self):
        self._neighbours = {}

    def add_edge(self, source: int, destination: int) -> None:
        self._neighbours[source] = destination

    @classmethod
    def from_edges_list(cls, edges: List[int]) -> "Graph":
        self = cls()
        for source, destination in enumerate(edges):
            if destination != -1:
                self.add_edge(source, destination)
        return self

    def bfs(self, start_node: int, num_nodes: int) -> List[int]:
        """Use bfs to calculate the shortest part from start to
        every other node"""
        shortest_paths = [-1] * num_nodes
        queue = deque()
        visited = set()
        start_item = QueueItem(node=start_node, distance=0)
        shortest_paths[start_node] = 0
        queue.append(start_item)
        visited.add(start_node)
        while queue:
            item = queue.popleft()
            if item.node in self._neighbours:
                next_node = self._neighbours[item.node]
                if next_node not in visited:
                    next_distance = item.distance + 1
                    next_item = QueueItem(node=next_node, distance=next_distance)
                    queue.append(next_item)
                    shortest_paths[next_node] = next_distance
                    visited.add(next_node)
        return shortest_paths


class Solution:
    def closest_meeting_node(self, edges: List[int], node_1: int, node_2: int) -> int:
        graph = Graph.from_edges_list(edges)
        num_nodes = len(edges)
        distances_1 = graph.bfs(node_1, num_nodes)
        distances_2 = graph.bfs(node_2, num_nodes)
        min_dist_map = defaultdict(list)
        for idx in range(num_nodes):
            dist_1 = distances_1[idx]
            dist_2 = distances_2[idx]
            if dist_1 != -1 and dist_2 != -1:
                dist = max(dist_1, dist_2)
                min_dist_map[dist].append(idx)
        if not min_dist_map:
            return -1
        min_dist = min(min_dist_map)
        return min(min_dist_map[min_dist])
