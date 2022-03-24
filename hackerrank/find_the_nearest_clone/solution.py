from collections import (
    defaultdict,
    deque,
)
from dataclasses import dataclass


@dataclass
class QueueItem:
    id: int
    distance: int


def depth_first_search(start_node_id, graph, nodes_with_colour):
    start_node = QueueItem(id=start_node_id, distance=0)

    # Instantiate the queue with the start node, which has distance    # 0 from itself
    queue = deque([start_node])
    visited = {start_node_id}

    while queue:
        next_node = queue.popleft()
        # Examine the nearest-neighbours of next_node, if
        # they haven't already been visited
        for neighbour in graph[next_node.id]:
            if neighbour not in visited:
                # neighbour has correct colour, return
                # number of hops from start_node
                if neighbour in nodes_with_colour:
                    return next_node.distance + 1
                # neighbour has incorrect colour,
                # mark it as visited and add it to
                # the queue
                visited.add(neighbour)
                queue.append(
                    QueueItem(
                        id=neighbour,
                        distance=next_node.distance + 1,
                    ),
                )


def find_shortest(graph_nodes, graph_from, graph_to, node_colours, target_colour):
    # The set of nodes which have the target_colour
    nodes_with_target_colour = {idx + 1 for idx, n in enumerate(node_colours) if n == target_colour}

    # The graph representation is a dict, where each node has a key, and the corresponding
    # value is the set of nodes it shares an edge with.
    graph = defaultdict(set)
    for edge in range(len(graph_from)):
        vertex_from, vertex_to = graph_from[edge], graph_to[edge]
        graph[vertex_from].add(vertex_to)
        graph[vertex_to].add(vertex_from)

    # Short-circuit: if no nodes have the target_colour, or if only one does,
    # return early
    if len(nodes_with_target_colour) < 2:
        return -1

    # depth_first_search takes a start_node, and returns the distance to
    # the nearest node with the same (target) colour. Every node with the
    # target_colour needs to take a turn being the start_node, so we keep
    # track of its shortest (local) path and take the minimum of those at the end.
    path_lengths = set()
    for start_node in nodes_with_target_colour:
        path_length = depth_first_search(start_node, graph, nodes_with_target_colour)
        path_lengths.add(path_length)

    return min(path_lengths)
