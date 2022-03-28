def repeated_string(sub_string, n):
    s_len = len(sub_string)
    num_whole_substrings = n // s_len
    leftover_characters = n % s_len
    leftover_substring = sub_string[:leftover_characters]
    return num_whole_substrings * sub_string.count('a') + leftover_substring.count('a')
