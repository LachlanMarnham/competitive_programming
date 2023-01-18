def count_swaps(arr):
    n = len(arr)
    swaps = 0
    for j in range(n):
        for i in range(1, n - j):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                swaps += 1
    return swaps, arr[0], arr[-1]
