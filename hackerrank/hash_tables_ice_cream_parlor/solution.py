from collections import defaultdict


def what_flavours(cost, money):
    # Build a map of unique cost -> indices (indexed-1)
    cost_idx_map = defaultdict(list)
    for idx, val in enumerate(cost):
        cost_idx_map[val].append(idx + 1)

    for cost_1, idx_1_list in cost_idx_map.items():
        cost_2 = money - cost_1
        if cost_2 == cost_1:
            # If cost_1 is half of money, their
            # either needs to be a second item with
            # that cost, or else cost_1 doesn't appear
            # in the sale
            if len(idx_1_list) > 1:
                # From the uniqueness of the solution,
                # it follows that idx_1_list has length
                # 2 inside this suite
                idx_1, idx_2 = idx_1_list
                break
            else:
                continue
        elif cost_2 in cost_idx_map.keys():
            # From the uniqueness of the solution, it
            # follows that there can be only one item of
            # each price
            idx_1 = idx_1_list.pop()
            idx_2 = cost_idx_map[cost_2].pop()
            break

    # The smaller of the indices is meant to appear first
    # in the result
    if idx_1 < idx_2:
        message = f"{idx_1} {idx_2}"
    else:
        message = f"{idx_2} {idx_1}"

    return message
