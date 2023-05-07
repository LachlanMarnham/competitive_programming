class Solution:
    def max_vowels(self, s: str, k: int) -> int:
        VOWELS = {"a", "e", "i", "o", "u"}
        max_count = 0
        for letter in s[:k]:
            if letter in VOWELS:
                max_count += 1

        count = max_count
        for start in range(1, len(s) - k + 1):
            if s[start - 1] in VOWELS:
                count -= 1
            if s[start + k - 1] in VOWELS:
                count += 1
            if count > max_count:
                max_count = count

        return max_count
