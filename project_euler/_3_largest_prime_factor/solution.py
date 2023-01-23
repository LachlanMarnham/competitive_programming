from math import ceil, sqrt


def is_factor(num: int, factor: int) -> bool:
    return num % factor == 0


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def main():
    target = 600851475143
    max_factor = ceil(sqrt(target))
    largest_prime_factor = 0
    for i in range(1, max_factor):
        if is_factor(target, i) and is_prime(i):
            largest_prime_factor = i
    return largest_prime_factor
