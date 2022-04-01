def index_power(array: list, n: int) -> int:
    if n >= len(array):
        return -1
    return array[n] ** n
