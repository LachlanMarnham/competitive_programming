def maximum_toys(prices, k):
    prices.sort()
    num_toys = 0
    total = 0
    for price in prices:
        if total + price > k:
            return num_toys
        else:
            total += price
            num_toys += 1
    return num_toys
