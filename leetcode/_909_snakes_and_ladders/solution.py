from collections import deque
from dataclasses import dataclass
from typing import List


@dataclass
class QueueItem:
    position: int
    rolls: int


class Graph:
    def __init__(self) -> None:
        self._neighbours = {}

    def add_edge(self, a: int, b: int) -> None:
        self._neighbours[a] = b

    @classmethod
    def from_board(cls, board: List[List[int]]):
        self = cls()
        source = 0
        for idx, row in enumerate(board[::-1]):
            if idx % 2 == 0:
                start = 0
                stop = len(row)
                step = 1
            else:
                start = len(row) - 1
                stop = 0 - 1
                step = -1
            for j in range(start, stop, step):
                source += 1
                target = row[j]
                if target != -1:
                    self.add_edge(source, target)
        return self

    def find_shortest_game(self, n: int) -> int:
        # Optimisation: if there are no snakes or ladders
        # on the board, the fastest path is to roll a 6
        # every time
        if not self._neighbours:
            return (n**2 - 1) // 6 + 1
        start_position = QueueItem(position=1, rolls=0)
        visited = set()
        queue = deque()
        queue.append(start_position)
        while queue:
            next_item = queue.popleft()
            curr = next_item.position
            visited.add(curr)
            rolls = next_item.rolls
            # Stop condition: we have reached the final
            # position
            if curr == n**2:
                return rolls
            for next_square in range(curr + 1, min(curr + 6, n**2) + 1):
                # If there is a snake or ladder starting at next_square,
                # replace that square with the destination
                next_square = self._neighbours.get(next_square, next_square)
                if next_square not in visited:
                    queue_item = QueueItem(position=next_square, rolls=rolls + 1)
                    queue.append(queue_item)

        # It's not possible to reach the end
        return -1


class Solution:
    def snakes_and_ladders(self, board: List[List[int]]) -> int:
        n = len(board)
        graph = Graph.from_board(board)
        return graph.find_shortest_game(n)
