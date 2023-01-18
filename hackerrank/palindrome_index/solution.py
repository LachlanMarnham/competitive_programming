def is_palindrome(s, length):
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True


def palindrome_index(s):
    length = len(s)
    if is_palindrome(s, length):
        return -1
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            sub_str = s[:i] + s[i + 1 :]
            if is_palindrome(sub_str, length - 1):
                return i
            sub_str = s[: length - i - 1] + s[length - i :]
            if is_palindrome(sub_str, length - 1):
                return length - i - 1
    return -1
