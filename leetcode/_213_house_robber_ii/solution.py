from typing import List


class Solution:
    def _rob(self, nums: List[int]) -> int:
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

    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        # Note, this is the same as "198: House Robber", which was
        # for a street without loops. Now, instead of running through
        # the street from start to end, we run through it twice:
        # the first run-through excludes the very first house, and the second
        # run through excludes the very last house. Since the street is now a
        # circle, the first and last houses are now adjacent. So there are two
        # possible sets of trajectories: those that pass through house 0 and not
        # house -1, and those which pass through -1 but not 0.
        answer_1 = self._rob(nums[1:])
        answer_2 = self._rob(nums[:-1])
        return max(answer_1, answer_2)
