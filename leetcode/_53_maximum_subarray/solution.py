from typing import List


class Solution:
    def max_sub_array(self, nums: List[int]) -> int:
        if all(num < 0 for num in nums):
            return max(nums)
        elif all(num > 0 for num in nums):
            return sum(nums)

        best_sum = -float("inf")
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum + num)
            best_sum = max(best_sum, current_sum)
        return best_sum
