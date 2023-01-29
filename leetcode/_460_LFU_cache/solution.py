from collections import defaultdict, deque
from dataclasses import dataclass


@dataclass
class CacheItem:
    key: int
    value: int
    frequency: int = 1


class LFUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._items_count = 0
        self._cache = {}
        self._frequency_to_items = defaultdict(deque)
        self._min_frequency = 1

    def _touch(self, item: CacheItem):
        old_frequency = item.frequency
        new_frequency = old_frequency + 1
        self._frequency_to_items[old_frequency].remove(item.key)
        
        if not self._frequency_to_items[old_frequency] and old_frequency == self._min_frequency:
            self._min_frequency += 1
            
        self._frequency_to_items[new_frequency].appendleft(item.key)
        item.frequency = new_frequency

    def get(self, key: int) -> int:
        if key in self._cache:
            item = self._cache[key]
            self._touch(item)
            return item.value
        return -1

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return

        item = self._cache.get(key)
        if item is not None:
            item.value = value
            self._touch(item)
            return
