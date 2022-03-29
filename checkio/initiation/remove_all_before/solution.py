def remove_all_before(items: list, border: int) -> list:
    if border not in items:
        return items
    border_idx = items.index(border)
    return items[border_idx:]
