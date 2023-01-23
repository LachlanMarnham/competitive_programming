from typing import List


class Solution:
    def find_median_sorted_arrays(self, nums_1: List[int], nums_2: List[int]) -> float:
        nums = []
        length = 0
        while nums_1 and nums_2:
            if nums_1[0] < nums_2[0]:
                val = nums_1.pop(0)
            else:
                val = nums_2.pop(0)
            nums.append(val)
            length += 1
        for val in nums_1:
            nums.append(val)
            length += 1
        for val in nums_2:
            nums.append(val)
            length += 1
        mid, is_odd = divmod(length, 2)
        if is_odd:
            return nums[mid]
        else:
            return (nums[mid] + nums[mid - 1]) / 2
