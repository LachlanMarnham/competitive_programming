from collections import defaultdict


def sort_key(frequency_map, first_appeared_map):
    def _sort_key(item):
        """when list.sort is called on a list of tuples,
        the sort order is determined by the 0th element of each
        tuple. If two tuples have the same 0th element, then the
        1st element of each is used to sort among them, and so on
        to the nth element.
        For this problem, elements should be sorted in order of
        highest to lowest frequency, and if two different items
        have the same frequency, they should remain in the same
        order in which they first appeared.
        Therefore, since we call list.sort with reverse=True,
        the tuple for each item should have a 0th element which
        *increases* as the frequency increases, and a 1st element
        which *decreases* as the first-appeared index increases
        """
        return frequency_map[item], -first_appeared_map[item]

    return _sort_key


def frequency_sort(items):
    frequency_map = defaultdict(int)
    first_appeared_map = dict()

    for idx, item in enumerate(items):
        frequency_map[item] += 1
        if item not in first_appeared_map:
            first_appeared_map[item] = idx
    items.sort(key=sort_key(frequency_map, first_appeared_map), reverse=True)
    return items
