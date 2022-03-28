def minimum_bribes(q):
    bribes = 0

    for i in range(len(q)):
        # q[i] is the initial position of
        # the ith person and i + 1 is their
        # current position (because the positions
        # are indexed-1). If they differ by more than
        # 2, too many bribes have been paid
        if q[i] - i - 1 > 2:
            return 'Too chaotic'

        # Every time we find a person with a higher
        # number standing in front of someone with
        # a lower number a bribe has been paid. Because
        # each person can pay at most two bribes, the inner
        # loop only has to look two deep
        for j in range(max(q[i] - 2, 0), i):
            if q[j] > q[i]:
                bribes += 1

    else:
        return bribes
