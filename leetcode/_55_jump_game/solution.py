from typing import List


class Solution:
    def can_jump(self, nums: List[int]) -> bool:
        accessible = -1

        for idx, val in enumerate(nums):
            if idx + val > accessible:
                accessible = idx + val
                if accessible >= len(nums) - 1:
                    return True
            if idx == accessible:
                return False
        return False
