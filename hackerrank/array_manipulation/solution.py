def array_manipulation(n, queries):
    arr = [0] * n

    # We don't need to add the increment to
    # every item in the [start, end] interval.
    # Instead, we can just add it to the beginning,
    # and subtract it again from the end.
    for start, end, increment in queries:
        arr[start - 1] += increment
        if end != n:
            arr[end] -= increment

    # Because we only incremented/decremented at the
    # beginning/end of the interval above, we can now
    # find the maximum value by keeping a running total
    # in a single pass of the array.
    current_sum = 0
    current_max = 0
    for val in arr:
        current_sum += val
        if current_sum > current_max:
            current_max = current_sum
    return current_max
