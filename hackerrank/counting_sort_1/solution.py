def counting_sort(arr):
    result = [0] * 100
    for val in arr:
        result[val] += 1
    return result
