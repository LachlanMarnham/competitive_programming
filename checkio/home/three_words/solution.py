def three_words(words: str) -> bool:
    count = 0
    for item in words.split():
        if item.isalpha():
            count += 1
        else:
            count = 0
        if count == 3:
            return True
    return False
