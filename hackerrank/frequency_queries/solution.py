def freq_query(queries):
    frequency_map = {}
    results = []
    for cmd, val in queries:
        if cmd == 1:
            if val not in frequency_map:
                frequency_map[val] = 0
            frequency_map[val] += 1
        elif cmd == 2:
            if val in frequency_map and frequency_map[val] > 0:
                frequency_map[val] -= 1
        elif cmd == 3:
            if val in frequency_map.values():
                results.append(1)
            else:
                results.append(0)
    return results
