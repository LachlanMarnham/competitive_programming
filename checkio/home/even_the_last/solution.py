def even_last(array: list) -> int:
    multiplier = array[-1] if array else 1
    return sum(array[::2]) * multiplier
