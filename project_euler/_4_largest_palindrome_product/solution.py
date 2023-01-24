def is_palindrome(num: int) -> bool:
    num_str = str(num)
    return num_str == num_str[::-1]


def main():
    largest = 1
    # The inner loop only checks values in
    # the range [i, 999] so we don't end up
    # calculating both a * b and b * a
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            # Only check is_palindrome if the product
            # is larger than the current largest (because
            # is_palindrome is the more expensive operation)
            if product > largest and is_palindrome(product):
                largest = product
    return largest
