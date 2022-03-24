#!/bin/python3


from collections import defaultdict, deque

# Complete the findShortest function below.

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] to <name>_to[i].
#
#
def bfs(node, nodes_with_colour, node_edge_map):
    queue = deque([(node, 0)])
    visited = set()
    while queue:
        current, count = queue.popleft()
        visited.add(current)
        for x in node_edge_map[current]:
            if x not in visited:
                if x in nodes_with_colour:
                    return count + 1
                else:
                    visited.add(x)
                    queue.append((x, count+1))


def findShortest(graph_nodes, graph_from, graph_to, ids, val):
    # Create the list of all nodes which have the target colour
    nodes_with_colour = []
    for idx, colour in enumerate(ids):
        if colour == val:
            nodes_with_colour.append(idx + 1)

    # Create the representation of the graph: each key is a
    # node, each value is a set of all nodes with which the key
    # shares an edge
    node_edge_map = defaultdict(set)
    for i in range(len(graph_from)):
        node_edge_map[graph_from[i]].add(graph_to[i])
        node_edge_map[graph_to[i]].add(graph_from[i])

    # Short-circuit: if there aren't at least 2 nodes
    # with the target colour, we can't find a path
    if len(nodes_with_colour) < 2:
        return -1

    # Path length with have an item for each starting node,
    # the value being the length of the shortest path to a
    # node of the same colour
    path_lengths = []

    for node in nodes_with_colour:
        path_length = bfs(node, nodes_with_colour, node_edge_map)
        path_lengths.append(path_length)

    return min(path_lengths)
