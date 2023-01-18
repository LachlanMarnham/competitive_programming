def super_digit(n, k):
    a = sum([int(i) for i in n])
    a = str(a * k)
    while len(a) != 1:
        temp = sum([int(i) for i in a])
        a = str(temp)
    return int(a)
