from typing import Iterable


def remove_all_after(items: list, border: int) -> Iterable:
    if not items or border not in items:
        return items
    idx = items.index(border)
    return items[:idx + 1]
