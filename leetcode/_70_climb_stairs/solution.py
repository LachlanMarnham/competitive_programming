class Solution:
    def climb_stairs(self, n: int) -> int:
        cache = {}
        for step in reversed(range(n)):
            if step == n - 1:
                cache[step] = 1
            elif step == n - 2:
                cache[step] = 1 + cache[step + 1]
            else:
                cache[step] = cache[step + 1] + cache[step + 2]
        return cache[0]
