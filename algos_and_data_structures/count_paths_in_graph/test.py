from .depth_first_search import Graph


def test():
    graph = Graph(5)
    graph.add_edge(0, 1)
    graph.add_edge(0, 4)
    graph.add_edge(0, 2)
    graph.add_edge(1, 4)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 2)
    assert graph.count_paths(0, 4) == 4
    assert graph.count_paths(0, 2) == 2
