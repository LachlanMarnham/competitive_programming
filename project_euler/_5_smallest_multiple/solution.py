def main():
    MAX_DIVISOR = candidate = 20
    # We only need to check the numbers between 11 and 20
    # For all i in [1, 10], 2i is guaranteed to be on [11, 20]
    # For all i in [11, 20], 2i > 20. So we need to check all
    # i in [11, 20], and no other possible divisors.
    # Also numbers which have a larger divisor and more spread out.
    # so iterate through them backwards to minimise the number of
    # operations
    MIN_DIVISOR = MAX_DIVISOR // 2
    # We will start at 20 and increment by 20, so every candidate
    # is guaranteed to be divisible by 20. So only try [11, 19]
    divisors = tuple(range(MAX_DIVISOR - 1, MIN_DIVISOR, -1))
    while True:
        for i in divisors:
            if candidate % i != 0:
                candidate += 20
                break
        else:
            return candidate
