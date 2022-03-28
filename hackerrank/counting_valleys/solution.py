def counting_valleys(path):
    elevation = 0
    valleys = 0

    for this_step in path:
        # Increment/decrement the elevation depending
        # on the direction of the current step
        if this_step == 'U':
            elevation += 1
            if elevation == 0:
                # If we are currently at sea-level,
                # having just moved up, we have just left
                # a valley
                valleys += 1
        else:
            elevation -= 1

    return valleys
