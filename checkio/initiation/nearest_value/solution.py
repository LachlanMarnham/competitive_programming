def nearest_value(values: set, target: int) -> int:
    candidate = candidate_distance = None

    for val in values:
        if val == target:
            return target
        if candidate_distance is None:
            candidate = val
            candidate_distance = abs(candidate - target)
            continue
        val_distance = abs(val - target)

        # We want the number closest to target. But if two
        # numbers have the same distance to target, we should
        # pick the lesser of the two.
        should_update = (
            val_distance < candidate_distance or
            val_distance == candidate_distance and
            val < candidate
        )

        if should_update:
            candidate = val
            candidate_distance = val_distance
    return candidate
