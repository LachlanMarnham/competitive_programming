def main():
    n = 100
    # https://www.cuemath.com/algebra/sum-of-squares/
    sum_of_squares = n * (n + 1) * (2 * n + 1) / 6

    # https://en.wikipedia.org/wiki/1_%2B_2_%2B_3_%2B_4_%2B_%E2%8B%AF
    sum_nums = n * (n + 1) / 2
    return sum_nums**2 - sum_of_squares
