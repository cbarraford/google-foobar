def answer(pegs):
    # no need to check ratios that are too large to fit on the first peg.
    maximum = pegs[1] - pegs[0] - 1
    for x in xrange(1, maximum):
        # calculate our gear sizes given the first size is x
        gear_sizes = [x]
        for peg in xrange(1, len(pegs)):
            gear_sizes.append(pegs[peg] - (pegs[peg-1] + gear_sizes[-1]))

        # if any of the gear_sizes are zero or negative, this can't be a potential because obviously
        # we can't have a non-existent gear. This isn't our answer, so skip this and try the next
        # one.
        if any(d <= 0 for d in gear_sizes):
            continue

        # see if we got an exact 2/1 match
        if x == 2 * gear_sizes[-1]:
            return [x, 1]

        # test if we have a ratio that works with 3 as the denominator
        if x+1 == 2 * gear_sizes[-1]:
            return [(x * 3) + 1, 3]
        if x+2 == 2 * gear_sizes[-1]:
            return [(x * 3) + 2, 3]

    return [-1, -1]
