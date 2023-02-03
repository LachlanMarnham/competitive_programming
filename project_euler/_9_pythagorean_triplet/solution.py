def is_triplet(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


def main():
    # a < b < c, so the closest the numbers
    # can be are b = a + 1 and c = b + 1. That
    # implies that a + b + c = 3 * a + 3 = 1000,
    # so a < (1000 - 3) / 3
    for a in range(1, (1000 - 3) // 3):
        # b must be larger than a, but its max value
        # is bound by the fact that b < c. b is maximised
        # when c = b + 1, therefore a + b + (b + 1) = 1000,
        # or equivalently, b < (1000 - a - 1) / 2
        for b in range(a, (1000 - a - 1) // 2):
            c = 1000 - a - b
            if is_triplet(a, b, c):
                return a * b * c
