def split_pairs(a):
    if len(a) % 2 != 0:
        a += '_'

    return [a[idx:idx + 2] for idx in range(0, len(a), 2)]
