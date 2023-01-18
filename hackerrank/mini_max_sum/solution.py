def mini_max_sum(arr):
    """By pre-sorting the list, the min sum of 4 numbers
    becomes the sum of the first 4 numbers, and the max
    sum of 4 numbers becomes the sum of the last 4
    numbers"""
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    return [min_sum, max_sum]
