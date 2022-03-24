#!/bin/python3

import math
import os
import random
import re
import sys
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
                queue.append((neighbour, distance+1))


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

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    graph_nodes, graph_edges = map(int, input().split())

    graph_from = [0] * graph_edges
    graph_to = [0] * graph_edges

    for i in range(graph_edges):
        graph_from[i], graph_to[i] = map(int, input().split())

    ids = list(map(int, input().rstrip().split()))

    val = int(input())

    ans = findShortest(graph_nodes, graph_from, graph_to, ids, val)

    fptr.write(str(ans) + '\n')

    fptr.close()
