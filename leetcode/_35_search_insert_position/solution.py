from typing import List


class Solution:
    def search_insert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums) - 1)

    def binary_search(self, arr, target, low, high):
        if low > high:
            return high + 1
        else:
            mid = (low + high) // 2
            if target == arr[mid]:
                return mid
            elif target > arr[mid]:  # x is on the right side
                return self.binary_search(arr, target, mid + 1, high)
            else:  # x is on the left side
                return self.binary_search(arr, target, low, mid - 1)
