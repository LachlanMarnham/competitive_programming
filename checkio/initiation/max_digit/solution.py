def max_digit(number: int) -> int:
    current_max = 0
    while number:
        remainder = number % 10
        if remainder > current_max:
            current_max = remainder
        # As soon as we find a 9 in
        # the number, we're done
        if current_max == 9:
            return current_max
        number //= 10
    return current_max
