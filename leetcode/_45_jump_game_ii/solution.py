from collections import defaultdict, deque
from dataclasses import dataclass
from typing import List


@dataclass
class QueueItem:
    node: int
    jumps: int


class Graph:
    def __init__(self) -> None:
        self._neighbours = defaultdict(list)

    @classmethod
    def from_jumps(cls, jumps: List[int]) -> None:
        self = cls()
        for start, max_jump in enumerate(jumps):
            for stop in range(start + 1, start + max_jump + 1):
                self._neighbours[start].append(stop)
        return self

    def get_min_jumps(self, destination: int) -> int:
        queue = deque()
        start = QueueItem(node=0, jumps=0)
        queue.append(start)
        visited = {start.node}
        while queue:
            item = queue.popleft()
            if item.node == destination:
                return item.jumps
            for neighbour in self._neighbours[item.node]:
                if neighbour not in visited:
                    new_item = QueueItem(node=neighbour, jumps=item.jumps + 1)
                    queue.append(new_item)
                    visited.add(new_item.node)


class Solution:
    def jump(self, nums: List[int]) -> int:
        graph = Graph.from_jumps(nums)
        return graph.get_min_jumps(len(nums) - 1)
