def tower_breakers(n, m):
    if m == 1:
        return 2
    if n % 2:
        return 1
    return 2
