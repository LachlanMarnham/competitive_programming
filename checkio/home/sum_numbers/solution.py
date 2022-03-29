def sum_numbers(text: str) -> int:
    total = 0
    for word in text.split():
        if word.isdigit():
            total += int(word)
    return total
