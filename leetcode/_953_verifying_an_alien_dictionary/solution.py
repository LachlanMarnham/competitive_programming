from string import ascii_lowercase
from typing import List


class Solution:
    def __init__(self) -> None:
        self._order_mapping = {}

    def _build_order_mapping(self, order: str) -> None:
        for idx, char in enumerate(order):
            self._order_mapping[char] = ascii_lowercase[idx]

    def _map_word(self, word: str) -> str:
        letters = []
        for char in word:
            letters.append(self._order_mapping[char])
        return "".join(letters)

    def is_alien_sorted(self, words: List[str], order: str) -> bool:
        self._build_order_mapping(order)
        idx = 0
        for word in sorted(words, key=self._map_word):
            if word != words[idx]:
                return False
            idx += 1
        return True
