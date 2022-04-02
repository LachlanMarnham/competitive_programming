def replace_last(line: list) -> list:
    if not line:
        return line
    last_element = line.pop()
    line.insert(0, last_element)
    return line
