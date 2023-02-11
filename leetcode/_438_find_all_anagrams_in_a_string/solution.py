from collections import Counter
from typing import List


class Solution:
    def find_anagrams(self, s: str, p: str) -> List[int]:
        len_p, len_s = len(p), len(s)
        if len_p > len_s:
            return []
        p_counter = Counter(p)
        s_counter = Counter(s[:len_p])
        indexes = []
        if p_counter == s_counter:
            indexes.append(0)
        for idx in range(len_s - len_p):
            s_counter[s[idx]] -= 1
            s_counter[s[len_p + idx]] += 1
            if p_counter == s_counter:
                indexes.append(idx + 1)
        return indexes
