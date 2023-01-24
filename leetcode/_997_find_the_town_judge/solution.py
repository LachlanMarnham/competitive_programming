from typing import List


class Solution:
    def find_judge(self, n: int, trust: List[List[int]]) -> int:
        people = set()
        trust_counter = {}
        for truster, trustee in trust:
            people.add(truster)
            if trustee not in trust_counter:
                trust_counter[trustee] = 0
            trust_counter[trustee] += 1
        for i in range(1, n + 1):
            if i not in people and trust_counter.get(i, 0) == n - 1:
                return i
        return -1
