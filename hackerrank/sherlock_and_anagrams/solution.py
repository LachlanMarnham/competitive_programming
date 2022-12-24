from collections import defaultdict


def generate_substrings(s):
    len_s = len(s)
    sub_strings = []
    for i in range(len_s):
        for j in range(len_s - i):
            new_substring = s[i : i + j + 1]
            sub_strings.append(new_substring)
    return sub_strings


def get_number_of_pairs(counter):
    """Counter maps sorted_substring -> instances(sorted_substring).
    for a substring occurs i times, the number of anagrams is the sum of
    all of the integers from 1 to i-1 (inclusive). Why is this? Imagine
    a collection of i identical items, then the problem reduces to the
    number of (unique) arrows we can draw between the items. The way to
    programatically do this is to start with the first item, and draw
    an arrow to all of the other i - 1 items. Now go to the second, and
    draw an arrow to each of the other i - 2 items. We will end up with a
    total of (i - 1) + (i - 2) + ... + 1 arrows. Luckily, there is a result
    due to Gauss to help calculate the sum of all integers on the interval
    [1, n]"""
    return sum(gauss(i - 1) for i in counter.values())


def gauss(n):
    """There is a theorem due to Gauss that the sum of
    the numbers on the interval [1, n] is n * (n + 1) / 2.
    The solution will always be an integer, so we use integer
    division to prevent the int -> float type conversion."""
    return n * (n + 1) // 2


def sherlock_and_anagrams(s):
    sub_strings = generate_substrings(s)
    counter = defaultdict(int)
    for sub_string in sub_strings:
        sorted_substring = str(sorted(sub_string))
        counter[sorted_substring] += 1
    return get_number_of_pairs(counter)
