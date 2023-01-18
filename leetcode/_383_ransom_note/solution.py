class Solution:
    def can_construct(self, ransom_note: str, magazine: str) -> bool:
        magazine_frequencies = {}
        for letter in magazine:
            if letter not in magazine_frequencies:
                magazine_frequencies[letter] = 0
            magazine_frequencies[letter] += 1

        ransom_frequencies = {}
        for letter in ransom_note:
            if letter not in ransom_frequencies:
                ransom_frequencies[letter] = 0
            ransom_frequencies[letter] += 1

        for letter, ransom_count in ransom_frequencies.items():
            magazine_count = magazine_frequencies.get(letter, 0)
            if ransom_count > magazine_count:
                return False
        return True
