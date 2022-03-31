def split_list(items: list) -> list:
    num_items = len(items)
    return [
        items[:(num_items + 1) // 2],
        items[(num_items + 1) // 2:],
    ]
