from collections import defaultdict


def popular_words(text: str, words: list) -> dict:
    text = text.lower()
    frequency_map = defaultdict(int)

    for word in text.split():
        frequency_map[word] += 1

    return {key: frequency_map[key] for key in words}
