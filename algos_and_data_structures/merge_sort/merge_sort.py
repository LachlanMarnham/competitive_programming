def merge(left_arr, right_arr):
    # Note, this function is assumed to opperated
    # on two pre-sorted lists (`left_arr` and
    # `right_arr`)
    merged_arr = []

    # Consider the first element of each array.
    # Whichever is smallest of the two gets removed
    # and added to `merged_arr`. Since `left_arr` and
    # `right_arr` are pre-sorted by assumption, this
    # means `merged_arr` is sorted too. Continue until
    # either `left_arr` or `right_arr` is empty
    while left_arr and right_arr:
        if left_arr[0] < right_arr[0]:
            el = left_arr.pop(0)
        else:
            el = right_arr.pop(0)
        merged_arr.append(el)

    # At this point either `left_arr` or `right_arr`
    # is empty. Since each of these is pre-sorted,
    # any remaining elements can be added to the end of
    # `merged_arr`
    merged_arr.extend(left_arr)
    merged_arr.extend(right_arr)
    return merged_arr


def merge_sort(arr):
    n = len(arr)

    # If the array only contains one element,
    # do nothing (recursion base case).
    # if the array contains more than one element,
    # break it in two, sort each of them (recursively)
    # and merge the results. Here, merge is assumed
    # to be an operation which takes two pre-sorted
    # arrays and merges them into a new (sorted) array.
    if n == 1:
        return arr
    mid = n // 2
    left_arr = merge_sort(arr[:mid])
    right_arr = merge_sort(arr[mid:])
    return merge(left_arr, right_arr)
