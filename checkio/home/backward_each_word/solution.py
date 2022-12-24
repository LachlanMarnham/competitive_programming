def backward_string_by_word(text: str) -> str:
    words = text.split(" ")
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)
