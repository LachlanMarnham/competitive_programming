from collections import defaultdict


def non_unique_elements(data: list) -> list:
    frequency_map = defaultdict(int)
    for datum in data:
        frequency_map[datum] += 1
    return [i for i in data if frequency_map[i] > 1]
