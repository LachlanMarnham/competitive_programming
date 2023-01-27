from typing import List, Set


class Solution:
    def is_concatenation(self, word: str, words: Set[str]) -> bool:
        for i in range(1, len(word)):
            left = word[:i]
            right = word[i:]
            if left in words:
                if right in words:
                    return True
                else:
                    if self.is_concatenation(right, words):
                        return True
                    else:
                        continue
        return False

    def find_concatenated_words(self, words: List[str]) -> List[str]:
        words = set(words)
        results = []
        for word in words:
            if self.is_concatenation(word, words):
                results.append(word)
        return results
