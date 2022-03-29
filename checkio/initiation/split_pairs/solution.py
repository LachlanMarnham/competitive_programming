def split_pairs(a):
    if len(a) % 2 != 0:
        a += '_'

    result = []
    for idx in range(0, len(a), 2):
        result.append(a[idx:idx + 2])
    return result
