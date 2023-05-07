from typing import List


class Solution:
    def array_sign(self, nums: List[int]) -> int:
        result = 1
        for val in nums:
            if val == 0:
                return 0
            if val < 0:
                result *= -1
        return result
