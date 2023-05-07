class Solution:
    def __init__(self):
        self._cache = {
            0: 0,
            1: 1,
        }

    def fib(self, n: int) -> int:
        if n in self._cache:
            return self._cache[n]
        fib_n = self.fib(n - 1) + self.fib(n - 2)
        self._cache[n] = fib_n
        return fib_n
