import re


def first_word(text: str) -> str:
    FIRST_WORD_PATTERN = r"^[^a-zA-Z']*(?P<first_word>[a-zA-Z']+).*$"
    match = re.search(FIRST_WORD_PATTERN, text).group("first_word")
    return match
