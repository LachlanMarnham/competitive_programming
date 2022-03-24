from collections import (
    defaultdict,
    deque,
)


def depth_first_search(start_node, graph, nodes_with_colour):
    queue = deque([(start_node, 0)])
    visited = {start_node}
    while queue:
        node, distance = queue.popleft()

        for neighbour in graph[node]:
            if neighbour not in visited:
                if neighbour in nodes_with_colour:
                    return distance + 1
                visited.add(neighbour)
                queue.append((neighbour, distance + 1))


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    nodes_with_colour = {idx + 1 for idx, n in enumerate(ids) if n == val}

    graph = defaultdict(set)
    for edge in range(len(graph_from)):
        vertex_from, vertex_to = graph_from[edge], graph_to[edge]
        graph[vertex_from].add(vertex_to)
        graph[vertex_to].add(vertex_from)

    if len(nodes_with_colour) < 2:
        return -1

    path_lengths = set()
    for start_node in nodes_with_colour:
        path_length = depth_first_search(start_node, graph, nodes_with_colour)
        path_lengths.add(path_length)

    return min(path_lengths)
