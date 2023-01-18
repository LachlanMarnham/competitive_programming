def between_markers(text: str, begin: str, end: str) -> str:
    begin_idx = text.find(begin)
    end_idx = text.find(end)

    if begin_idx == -1:
        begin_idx = 0
    else:
        begin_idx += len(begin)

    if end_idx == -1:
        end_idx = None

    return text[begin_idx:end_idx]
