from collections import Counter
from typing import List


class Solution:
    def delete_and_earn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        min_value, max_value = min(counter), max(counter)

        c_0 = c_1 = 0
        for i in range(min_value, max_value + 1):
            c_0, c_1 = c_1, max(c_0 + i * counter[i], c_1)

        return max(c_0, c_1)
