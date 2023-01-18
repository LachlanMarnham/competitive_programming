def pairs(k, arr):
    frequencies = {}
    for item in arr:
        if item not in frequencies:
            frequencies[item] = 1
        else:
            frequencies[item] += 1

    pairs = 0
    for val in arr:
        pairs += frequencies.get(val + k, 0)
        pairs += frequencies.get(val - k, 0)
    return pairs // 2
