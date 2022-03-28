def minimum_absolute_difference(arr):
    # Pre-sort the list. This way we only need to
    # compare adjacent items
    arr.sort()

    # Compute the absolute difference of each pair
    # of adjacent items
    differences = set()
    for idx in range(len(arr) - 1):
        val_1 = arr[idx]
        val_2 = arr[idx + 1]
        difference = abs(val_2 - val_1)
        differences.add(difference)

    # Return the minimum absolute difference
    return min(differences)
