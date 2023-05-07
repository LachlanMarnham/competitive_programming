from typing import List


class Solution:
    def find_difference(self, nums_1: List[int], nums_2: List[int]) -> List[List[int]]:
        answer = []
        nums_1, nums_2 = set(nums_1), set(nums_2)
        answer.append(list(nums_1 - nums_2))
        answer.append(list(nums_2 - nums_1))
        return answer
