from typing import Dict, List


class Solution:
    def build_index_map(self, nums: List[int]) -> Dict[int, List[int]]:
        index_map = {}
        for idx, num in enumerate(nums):
            if num not in index_map:
                index_map[num] = []
            index_map[num].append(idx)
        return index_map

    def two_sum(self, nums: List[int], target: int) -> List[int]:
        index_map = self.build_index_map(nums)
        for num_1, num_1_idxs in index_map.items():
            if float(num_1) == target / 2:
                if len(num_1_idxs) == 2:
                    return num_1_idxs
                else:
                    continue
            num_2 = target - num_1
            if num_2 in index_map:
                num_2_idx = index_map[num_2][0]
                num_1_idx = num_1_idxs[0]
                return [num_1_idx, num_2_idx]
