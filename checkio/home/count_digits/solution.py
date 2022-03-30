def count_digits(text: str) -> int:
    count = 0
    for letter in text:
        if letter.isdigit():
            count += 1
    return count
