def lonely_integer(arr):
    """The first time we see an element add it to
    `seen`. The second time we see an element remove
    it from `seen`. All elements but one occur twice, so
    at the end we should be left with only one element
    in `seen`."""
    seen = set()
    for item in arr:
        if item in seen:
            seen.remove(item)
        else:
            seen.add(item)
    return seen.pop()
