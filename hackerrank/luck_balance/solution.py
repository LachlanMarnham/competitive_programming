def luck_balance(k, contests):
    balance = 0
    lost = 0

    # Pre-sort the contests in decreasing order of
    # luck-balance
    contests.sort(key=lambda c: c[0], reverse=True)
    for luck, importance in contests:
        if importance == 0:
            balance += luck
        elif lost < k:
            balance += luck
            lost += 1
        else:
            balance -= luck

    return balance
