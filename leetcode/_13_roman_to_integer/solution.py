class Solution:

    symbols = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    def roman_to_int(self, s: str) -> int:
        length = len(s)
        result = 0
        for i in range(length):
            if i == length - 1:
                result += self.symbols[s[i]]
            else:
                a = self.symbols[s[i]]
                b = self.symbols[s[i + 1]]
                if a >= b:
                    result += a
                else:
                    result -= a
        return result
