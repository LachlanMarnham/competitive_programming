def hourglass_sum(arr):
    sums = set()
    length = width = 6
    for i in range(1, width - 1):
        for j in range(1, length - 1):
            a, b, c = arr[j - 1][i - 1:i + 2]
            d = arr[j][i]
            e, f, g = arr[j + 1][i - 1:i + 2]
            local_sum = a + b + c + d + e + f + g
            sums.add(local_sum)
    return max(sums)
