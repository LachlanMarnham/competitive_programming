from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return max(nums)
        plunder = [0] * n
        for i in range(n):
            if i < 2:
                plunder[i] = nums[i]
                continue
            elif i == 2:
                plunder[i] = nums[i] + plunder[i - 2]
                continue
            else:
                plunder[i] = nums[i] + max(plunder[i - 2], plunder[i - 3])
        return max(plunder[-2:])
