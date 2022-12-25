def diagonal_difference(arr):
    primary_sum = secondary_sum = 0
    length = len(arr)
    for i in range(length):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][length - i - 1]
    return abs(primary_sum - secondary_sum)
