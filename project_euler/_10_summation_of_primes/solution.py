def main():
    # Uses the Sieve of Eratosthenes
    MAX = 2_000_000
    composites = set()
    prime_sum = 0
    for candidate in range(2, MAX):
        if candidate not in composites:
            prime_sum += candidate
            for new_composite in range(2 * candidate, MAX, candidate):
                composites.add(new_composite)
    return prime_sum
