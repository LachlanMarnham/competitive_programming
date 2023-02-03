class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        n = len(s)
        if num_rows == 1 or num_rows >= n:
            return s
        row = 0
        next_idx = 0
        long_jump = 2 * num_rows - 2
        short_jump = 0
        long_jump_is_next = True
        letters = []
        while len(letters) < n:
            next_letter = s[next_idx]
            letters.append(next_letter)
            next_idx += long_jump if long_jump_is_next else short_jump
            if short_jump == 0:
                long_jump_is_next = True
            elif long_jump == 0:
                long_jump_is_next = False
            else:
                long_jump_is_next = not long_jump_is_next
            if next_idx >= n:
                row += 1
                next_idx = row
                long_jump -= 2
                short_jump += 2
                long_jump_is_next = True if long_jump != 0 else False
        return "".join(letters)
