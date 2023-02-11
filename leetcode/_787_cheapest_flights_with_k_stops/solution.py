import heapq
from collections import defaultdict
from dataclasses import dataclass
from typing import List


@dataclass
class Flight:
    src: int
    dest: int
    price: int


@dataclass
class QueueItem:
    node: int
    stops: int
    price: int

    def __lt__(self, other):
        return self.price < other.price


class Graph:
    def __init__(self):
        self._neighbours = defaultdict(list)

    @classmethod
    def from_flights(cls, flights: List[List[int]]) -> "Graph":
        self = cls()
        for src, dest, price in flights:
            flight = Flight(src=src, dest=dest, price=price)
            self._neighbours[src].append(flight)
        return self


class PriorityQueue(object):
    def __init__(self):
        self._data = []

    def push(self, item):
        heapq.heappush(self._data, (item.price, item))

    def pop(self):
        return heapq.heappop(self._data)[1]

    def __bool__(self):
        return bool(len(self._data))


class Solution:
    def find_cheapest_price(self, flights, src, dst, k):
        visited = {}
        graph = Graph.from_flights(flights)
        pq = PriorityQueue()
        pq.push(QueueItem(node=src, stops=0, price=0))
        while pq:
            item = pq.pop()
            cost, stops, node = item.price, item.stops, item.node
            if node == dst and stops - 1 <= k:
                return cost
            if node not in visited or visited[node] > stops:
                visited[node] = stops
                neighbours = graph._neighbours[node]
                for neighbour in neighbours:
                    new_item = QueueItem(node=neighbour.dest, stops=stops + 1, price=cost + neighbour.price)
                    pq.push(new_item)
        return -1
