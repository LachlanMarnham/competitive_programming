def two_strings(string_1, string_2):
    set_1 = set(string_1)
    set_2 = set(string_2)
    if set_1.intersection(set_2):
        return "YES"
    return "NO"
