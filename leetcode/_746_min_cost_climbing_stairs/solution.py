from typing import List


class Solution:
    def min_cost_climbing_stairs(self, cost: List[int]) -> int:
        cache = {}
        n = len(cost)
        for step in reversed(range(n)):
            if step >= n - 2:
                cache[step] = cost[step]
            else:
                this_cost = cost[step]
                cache[step] = this_cost + min(cache[step + 1], cache[step + 2])
        return min(cache[0], cache[1])
