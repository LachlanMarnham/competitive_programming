from collections import defaultdict, deque
from dataclasses import dataclass


@dataclass
class QueueItem:
    name: str
    distance: int


class Graph:
    def __init__(self, num_nodes):
        self._num_nodes = num_nodes
        self._neighbour_map = defaultdict(set)

    def connect(self, start_node, end_node):
        self._neighbour_map[start_node].add(end_node)
        self._neighbour_map[end_node].add(start_node)

    def _build_result_list(self, start_node, node_distance_map):
        result = []
        for node in range(self._num_nodes):
            if node != start_node:
                distance = node_distance_map.get(node, -1)
                result.append(distance)
        return result

    def find_all_distances(self, start_node):
        # key = node, val = distance
        visited = {}
        queue = deque()

        # mark start_node as visited and add it
        # to the queue
        visited[start_node] = 0
        start_item = QueueItem(
            name=start_node,
            distance=0,
        )
        queue.append(start_item)

        while queue:
            next_node = queue.popleft()
            neighbours = self._neighbour_map[next_node.name]
            for neighbour in neighbours:
                # If we have seen this node before, skip
                if neighbour in visited:
                    continue

                # Mark the node as visited, and record
                # its distance from the origin
                visited[neighbour] = next_node.distance + 6

                # Add the node to the queue so we can
                # explore its neighbours next
                neighbour_item = QueueItem(
                    name=neighbour,
                    distance=next_node.distance + 6,
                )
                queue.append(neighbour_item)

        result = self._build_result_list(start_node, visited)
        return " ".join(str(val) for val in result)
