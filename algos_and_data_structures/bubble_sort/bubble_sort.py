def bubble_sort(arr):
    n = len(arr)
    # `i` sweeps through the array and is used to
    # check adjacent elements so they can be swapped
    # if necessary.
    # After the first pass through (in the `i` loop),
    # the largest element will be in the correct place
    # at the end of the array. After the second pass through
    # the second largest element will be in the correct position
    # and so on. Therefore, `j` is used to constrain the `i` loop,
    # by making sure we only check elements which might be out of
    # position
    for j in range(n):
        swapped = False
        for i in range(1, n - j):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swapped = True
        # If we manage to go through an entire `i` loop
        # without swapping any elements then the list must
        # be sorted and we can stop. This makes the
        # best-case complexity `O(n)` (for a pre-sorted list)
        if swapped is False:
            break
    return arr
