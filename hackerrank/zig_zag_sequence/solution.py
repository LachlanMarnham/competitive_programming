def find_zig_zag_sequence(a, n):
    a.sort()
    mid = int((n + 1) / 2)
    a[mid - 1], a[n - 1] = a[n - 1], a[mid - 1]

    st = mid + 1
    ed = n - 1
    while st <= ed:
        a[st - 1], a[ed - 1] = a[ed - 1], a[st - 1]
        st = st + 1
        ed = ed - 1

    return a
