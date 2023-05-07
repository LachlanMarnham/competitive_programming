from typing import List


class Solution:
    def num_subseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        start_idx, end_idx = 0, len(nums) - 1
        count = 0
        mod = 10**9 + 7

        while start_idx <= end_idx:
            if nums[start_idx] + nums[end_idx] > target:
                end_idx -= 1
            else:
                count += pow(2, end_idx - start_idx, mod)
                start_idx += 1

        return count % mod
