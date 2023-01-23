def main():
    MAX_MULTIPLE = 1_000
    multiples = set()
    threes = 3
    fives = 5
    while threes < MAX_MULTIPLE:
        multiples.add(threes)
        threes += 3
        if fives < MAX_MULTIPLE:
            multiples.add(fives)
            fives += 5
    return sum(multiples)
