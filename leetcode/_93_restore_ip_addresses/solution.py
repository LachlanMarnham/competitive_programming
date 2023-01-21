from typing import List, Tuple


class Solution:
    def is_valid_field(self, s: str) -> bool:
        if len(s) > 1 and s.startswith("0"):
            return False
        elif 0 <= int(s) <= 255:
            return True
        return False

    def generate_field_sizes(self, s: str) -> Tuple[str, str, str, str]:
        min_size = 1
        max_size = 3
        for i in range(min_size, max_size + 1):
            for j in range(min_size, max_size + 1):
                for k in range(min_size, max_size + 1):
                    for l in range(min_size, max_size + 1):  # noqa: E741
                        if i + j + k + l == len(s):  # noqa: E741
                            yield i, j, k

    def generate_fields(self, s: str) -> Tuple[str, str, str, str]:
        for i, j, k in self.generate_field_sizes(s):
            a = s[:i]
            b = s[i : i + j]
            c = s[i + j : i + j + k]
            d = s[i + j + k :]
            yield a, b, c, d

    def restore_ip_addresses(self, s: str) -> List[str]:
        results = []
        if 4 <= len(s) <= 12:
            for fields in self.generate_fields(s):
                if all(self.is_valid_field(field) for field in fields):
                    ip_addr = ".".join(fields)
                    results.append(ip_addr)
        return results
