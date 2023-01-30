from math import sqrt


def is_prime(num: int) -> bool:
    for i in range(3, int(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    else:
        return True


def main() -> int:
    TARGET = 10_001
    prime_count = 1
    i = 3
    while True:
        if is_prime(i):
            prime_count += 1
            if prime_count == TARGET:
                return i
        i += 2
