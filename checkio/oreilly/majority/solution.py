def is_majority(items):
    if not items:
        return False
    if items.count(True) > len(items) / 2:
        return True
    return False
