from collections import defaultdict


def most_frequent(data: list) -> str:
    frequency_map = defaultdict(int)
    for word in data:
        frequency_map[word] += 1
    return max(frequency_map, key=frequency_map.__getitem__)
