def main():
    second_last = 1
    last = 2
    total = 0
    while last <= 4_000_000:
        if last % 2 == 0:
            total += last
        new_val = second_last + last
        second_last = last
        last = new_val
    return total
