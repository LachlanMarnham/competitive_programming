CACHE = {}


def step_perms(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif n in CACHE:
        return CACHE[n]
    else:
        options = step_perms(n - 1) + step_perms(n - 2) + step_perms(n - 3)
        CACHE[n] = options
        return options
