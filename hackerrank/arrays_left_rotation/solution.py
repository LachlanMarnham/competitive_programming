def rotLeft(arr, num_rotations):
    # arr is invariant under rotations modulo len(arr),
    # so we just need to find the excess/net rotation
    net_shift = num_rotations % len(arr)
    return arr[net_shift:] + arr[:net_shift]
