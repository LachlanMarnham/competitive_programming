class Solution:
    def divisible(self, string: str, sub_string: str, len_string: int, len_sub_string: int) -> bool:
        candidate = sub_string * (len_string // len_sub_string)
        if candidate == string:
            return True
        return False

    def get_common_divisors(self, num_1: int, num_2: int) -> int:
        # Note: by definition, num_2 > num_1
        for i in range(num_1 // 2, 0, -1):
            if num_1 % i == 0 and num_2 % i == 0:
                yield i

    def gcd_of_strings(self, str_1: str, str_2: str) -> str:
        # If the strings are the same, the largest sub-string
        # is equal to both of them
        if str_1 == str_2:
            return str_1

        # Make sure str_1 is the shorter of the two strings
        len_1 = len(str_1)
        len_2 = len(str_2)
        if len_1 > len_2:
            str_1, str_2 = str_2, str_1
            len_1, len_2 = len_2, len_1

        # If the strings aren't the same, the largest sub-string
        # might be the shorter of the two strings
        if len_2 % len_1 == 0 and self.divisible(str_2, str_1, len_2, len_1):
            return str_1

        # Get the common divisors of len_1 and len_2,
        # and for each GCD i try the substring which is the first
        # i characters of str_1
        for i in self.get_common_divisors(len_1, len_2):
            candidate = str_1[:i]
            if self.divisible(str_1, candidate, len_1, i) and self.divisible(str_2, candidate, len_2, i):
                return candidate
        return ""
