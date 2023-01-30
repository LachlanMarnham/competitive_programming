class Solution:
    _cache = {
        0: 0,
        1: 1,
        2: 1,
    }

    def tribonacci(self, n: int) -> int:
        if n in self._cache:
            return self._cache[n]
        else:
            result = self.tribonacci(n - 1) + self.tribonacci(n - 2) + self.tribonacci(n - 3)
            self._cache[n] = result
            return result
