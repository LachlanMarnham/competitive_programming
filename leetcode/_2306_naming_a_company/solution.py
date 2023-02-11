from collections import defaultdict
from typing import List


class Solution:
    def distinct_names(self, ideas: List[str]) -> int:
        prefix_groups = defaultdict(set)
        for idea in ideas:
            prefix = idea[0]
            suffix = idea[1:]
            prefix_groups[prefix].add(suffix)

        arr = list(prefix_groups.keys())
        count = 0
        for prefix_1 in arr:
            for prefix_2 in arr:
                if prefix_1 != prefix_2:
                    common = len(prefix_groups[prefix_1].intersection(prefix_groups[prefix_2]))
                    count += (len(prefix_groups[prefix_1]) - common) * (len(prefix_groups[prefix_2]) - common)

        return count
