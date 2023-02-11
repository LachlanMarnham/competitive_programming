from string import ascii_lowercase


class Solution:
    def check_inclusion(self, s1: str, s2: str) -> bool:
        len_s1 = len(s1)
        len_s2 = len(s2)
        if len_s1 > len_s2:
            return False

        freq_1 = dict.fromkeys(ascii_lowercase, 0)
        for c in s1:
            freq_1[c] += 1

        for i in range(len_s2 - len_s1 + 1):
            freq_2 = dict.fromkeys(ascii_lowercase, 0)
            for c in s2[i : len_s1 + i]:
                freq_2[c] += 1
            if freq_1 == freq_2:
                return True
        return False
