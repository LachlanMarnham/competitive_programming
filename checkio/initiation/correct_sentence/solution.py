def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]
    return text if text.endswith('.') else text + '.'
