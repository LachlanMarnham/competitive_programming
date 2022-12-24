from collections import defaultdict, deque
from dataclasses import dataclass


def is_safe(label):
    if label == 0:
        return True
    return False


def build_graph(clouds, num_clouds):
    graph = defaultdict(set)

    # From the point of view of the graph
    # representation only care about the connected
    # part, and can ignore the dangerous clouds
    for idx in range(num_clouds - 2):
        if is_safe(clouds[idx]):
            # if the nearest neighbour and/or the
            # next-nearest neighbour is also a
            # safe cloud, add an edge to the graph
            if is_safe(clouds[idx + 1]):
                graph[idx].add(idx + 1)
                graph[idx + 1].add(idx)
            if is_safe(clouds[idx + 2]):
                graph[idx].add(idx + 2)
                graph[idx + 2].add(idx)

    # The possible edge between the penultimate and
    # final clouds has to be handled seperately
    if is_safe(clouds[-2]):
        graph[num_clouds - 1].add(num_clouds - 2)
        graph[num_clouds - 2].add(num_clouds - 1)

    return graph


@dataclass
class QueueItem:
    name: str
    distance: int


def bfs(graph, start_cloud, end_cloud):
    queue = deque()
    visited = set()

    # Add the first cloud to the queue and
    # mark it as visited (to avoid cycles)
    start_item = QueueItem(
        name=start_cloud,
        distance=0,
    )
    queue.append(start_item)
    visited.add(start_item.name)

    while queue:
        next_cloud = queue.popleft()
        neighbour_distance = next_cloud.distance + 1
        neighbours = graph[next_cloud.name]
        for neighbour in neighbours:
            # If the neighbour has already been visited,
            # skip it to avoid cycles
            if neighbour in visited:
                continue
            # If we have reached the destination,
            # return the number of hops to get there
            if neighbour == end_cloud:
                return neighbour_distance
            # Otherwise, mark the neighbour as visited,
            # and add it to the queue
            visited.add(neighbour)
            neighbour_item = QueueItem(
                name=neighbour,
                distance=neighbour_distance,
            )
            queue.append(neighbour_item)


def jumping_on_clouds(c):
    num_clouds = len(c)
    graph = build_graph(c, num_clouds)
    shortest_path = bfs(graph, 0, num_clouds - 1)
    return shortest_path
