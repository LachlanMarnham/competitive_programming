from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)

        # min_jumps[i] is how many jumps it
        # takes to get from i to the end
        min_jumps = [10001] * n
        min_jumps[-1] = 0
        for i in range(n - 2, -1, -1):
            jump_i = nums[i]

            # It's possible to get from
            # i to the end in one jump
            if i + jump_i >= n - 1:
                min_jumps[i] = 1
            else:
                min_jumps[i] = min(min_jumps[i : i + jump_i + 1]) + 1
        return min_jumps[0]


# Old solution using BFS which was a bit slow...
# from collections import defaultdict, deque
# from dataclasses import dataclass


# @dataclass
# class QueueItem:
#     node: int
#     jumps: int


# class Graph:
#     def __init__(self) -> None:
#         self._neighbours = defaultdict(list)

#     @classmethod
#     def from_jumps(cls, jumps: List[int]) -> None:
#         self = cls()
#         for start, max_jump in enumerate(jumps):
#             for stop in range(start + 1, start + max_jump + 1):
#                 self._neighbours[start].append(stop)
#         return self

#     def get_min_jumps(self, destination: int) -> int:
#         queue = deque()
#         start = QueueItem(node=0, jumps=0)
#         queue.append(start)
#         visited = {start.node}
#         while queue:
#             item = queue.popleft()
#             if item.node == destination:
#                 return item.jumps
#             for neighbour in self._neighbours[item.node]:
#                 if neighbour not in visited:
#                     new_item = QueueItem(node=neighbour, jumps=item.jumps+1)
#                     queue.append(new_item)
#                     visited.add(new_item.node)


# class Solution:
#     def jump(self, nums: List[int]) -> int:
#         graph = Graph.from_jumps(nums)
#         return graph.get_min_jumps(len(nums) - 1)
