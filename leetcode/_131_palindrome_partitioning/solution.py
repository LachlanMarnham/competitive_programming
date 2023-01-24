from typing import List, Tuple


class Solution:
    def __init__(self) -> None:
        self.palindromes = set()
        self.semordnilaps = set()

    def is_palindrome(self, s: str) -> bool:
        if s in self.palindromes:
            return True
        elif s in self.semordnilaps:
            return False
        elif s != "" and s == s[::-1]:
            self.palindromes.add(s)
            return True
        else:
            self.semordnilaps.add(s)
            return False

    def partition_recursive(self, s: str) -> Tuple[str]:
        for i in range(len(s)):
            left_partition = s[: i + 1]
            right_partition = s[i + 1 :]
            if self.is_palindrome(left_partition):
                if self.is_palindrome(right_partition):
                    yield (left_partition, right_partition)
                elif not right_partition:
                    yield (left_partition,)
                for other_partitions in self.partition_recursive(right_partition):
                    result = (left_partition, *other_partitions)
                    yield result

    def partition(self, s: str) -> List[List[str]]:
        return [list(item) for item in set(self.partition_recursive(s))]
