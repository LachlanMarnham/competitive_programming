def sock_merchant(colour_arr):
    unpaired_colours = set()
    num_pairs = 0
    for colour in colour_arr:
        if colour in unpaired_colours:
            # We've seen an unpaired sock with
            # colour of val before. Remove
            # it (so there is at most one sock
            # per colour stored at each time)
            # and increment number of pairs
            unpaired_colours.remove(colour)
            num_pairs += 1
        else:
            # We haven't seen an unpaired sock
            # with this colour before, or we have
            # seen an integer number of pairs
            unpaired_colours.add(colour)
    return num_pairs
