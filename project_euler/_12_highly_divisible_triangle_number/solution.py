import math

cache = {1: 1}


def get_factors_count(n: int) -> int:
    global cache
    if n in cache:
        return cache[n]
    count = 0
    for i in range(1, math.ceil(math.sqrt(n))):
        if n % i == 0:
            count += 2
    cache[n] = count
    return count


def get_triangle_number(n: int) -> int:
    # Using Gauss' law of sum of first n integers
    return n * (n + 1) // 2


def find_first_with_target_factors(low: int, high: int, target: int):
    low_triangle = get_triangle_number(low)
    high_triangle = get_triangle_number(high)
    if get_factors_count(low_triangle) < target and get_factors_count(high_triangle) == target:
        return high
    mid = (high - low) // 2
    mid_triangle = get_triangle_number(mid)
    if get_factors_count(mid_triangle) >= target:
        return find_first_with_target_factors(low, mid, target)
    elif get_factors_count(mid_triangle) < target:
        return find_first_with_target_factors(mid, high, target)


def main():
    TARGET = 5
    low = 28
    high = 28
    while True:
        if get_factors_count(get_triangle_number(high)) > TARGET:
            return find_first_with_target_factors(low, high, TARGET)
        else:
            low = high
            high = 2 * high


print(main())
