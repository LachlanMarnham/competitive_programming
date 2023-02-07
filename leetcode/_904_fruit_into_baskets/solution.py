from collections import Counter
from typing import List


class Solution:
    def total_fruit(self, fruits: List[int]) -> int:
        num_trees = len(fruits)
        if num_trees <= 2:
            return len(fruits)

        counter = Counter([fruits[0]])
        left = 0
        right = 1
        current_max = 0
        while right < num_trees:
            counter[fruits[right]] += 1
            counter = +counter
            while len(counter) > 2:
                to_remove = fruits[left]
                counter[to_remove] -= 1
                if counter[to_remove] == 0:
                    del counter[to_remove]
                left += 1
            if right - left + 1 > current_max:
                current_max = right - left + 1
            right += 1
        return current_max
