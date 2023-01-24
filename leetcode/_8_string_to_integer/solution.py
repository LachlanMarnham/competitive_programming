import re


class Solution:
    def my_atoi(self, s: str) -> int:
        MIN = -(2**31)
        MAX = 2**31 - 1
        match = re.search(r"^\s*([+-]{0,1}\d+)", s)
        if match is None:
            return 0
        number = int(match.group(0))
        if number <= MIN:
            return MIN
        elif number >= MAX:
            return MAX
        else:
            return number
