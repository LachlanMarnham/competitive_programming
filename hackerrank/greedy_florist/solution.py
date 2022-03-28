def get_minimum_cost(num_friends, flower_costs):
    # Pre-sort and reverse the list so we
    # get the most-expensive flowers at the
    # largest discount
    flower_costs.sort(reverse=True)

    multiplier = 1
    total = 0
    for idx, cost in enumerate(flower_costs):
        total += cost * multiplier

        # If all of the friends have now
        # purchased the same number of flowers,
        # further purchases get more expensive
        if (idx + 1) % num_friends == 0:
            multiplier += 1

    return total
