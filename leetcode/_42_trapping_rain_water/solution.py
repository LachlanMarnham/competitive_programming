from typing import List, Tuple


class Solution:
    def _trim(self, heights: List[int]) -> Tuple[List[int], int]:
        """Remove any monotonically increasing section from the left,
        or any monotonically decreasing section from the right. Also returns
        the length of the new heights list, because calculating it here is
        cheaper than calling len(...) in self.trap."""
        n = len(heights)
        new_left = new_right = None
        for i in range(n - 1):
            if new_left is None and heights[i] > heights[i + 1]:
                new_left = i
            if new_right is None and heights[~i] > heights[~(i + 1)]:
                new_right = n - i - 1
        if new_left is None or new_right is None:
            return [], 0
        return heights[new_left : new_right + 1], new_right - new_left + 1

    def trap(self, heights: List[int]) -> int:
        heights, n = self._trim(heights)
        if n == 0:
            return 0
        left_peak = heights[0]
        right_peak = heights[n - 1]
        left_idx = 1
        right_idx = n - 2
        filled = 0
        while left_idx <= right_idx:
            if left_peak <= right_peak:
                left_peak = max(left_peak, heights[left_idx])
                filled += left_peak - heights[left_idx]
                left_idx += 1
            else:
                right_peak = max(right_peak, heights[right_idx])
                filled += right_peak - heights[right_idx]
                right_idx -= 1
        return filled
