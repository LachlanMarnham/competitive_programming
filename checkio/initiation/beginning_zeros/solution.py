def beginning_zeros(number: str) -> int:
    counter = 0
    for char in number:
        if char != "0":
            break
        counter += 1
    return counter
