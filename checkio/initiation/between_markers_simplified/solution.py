def between_markers(text: str, begin: str, end: str) -> str:
    begin_idx = text.index(begin)
    end_idx = text.index(end)
    return text[begin_idx + 1 : end_idx]
