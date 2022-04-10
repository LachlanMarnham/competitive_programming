from collections import defaultdict


def count_triplets(arr, r):
    triplets = 0
    middle_vals = defaultdict(int)
    terminator_vals = defaultdict(int)
    for k in arr:
        triplets += terminator_vals[k]
        terminator_vals[k * r] += middle_vals[k]
        middle_vals[k * r] += 1
    return triplets
