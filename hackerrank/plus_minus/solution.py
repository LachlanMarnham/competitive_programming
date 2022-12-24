def plus_minus(arr):
    length = len(arr)
    zeros = positives = negatives = 0

    for element in arr:
        if element > 0:
            positives += 1
        elif element < 0:
            negatives += 1
        else:
            zeros += 1

    return [
        f'{positives/length:.6f}',
        f'{negatives/length:.6f}',
        f'{zeros/length:.6f}',
    ]
