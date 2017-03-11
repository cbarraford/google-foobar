IMPOSSIBLE = "impossible"

# convert our numerical answer to a string, as the resulting answer always needs to be a string.
def result(num):
    return str(num)

def answer(M,F):
    iteration = 0
    # It is actually not important to track mach vs facula bombs, because if the inputs were
    # reversed (ie [F,M]), the answer would always be the same.
    bombset = [int(M), int(F)]

    # Quick exit 1
    # if both M and F are event numbers, there is no way we can get to (1,1) because subtracting an
    # even number with another even number will always result in an even number
    if bombset[0] % 2 == bombset[1] % 2 == 0:
        return IMPOSSIBLE

    # Quick exit 2
    # if machs and faculas are equal, there is no answer, unless we're already at (1,1)
    if bombset[0] == bombset[1]:
        if bombset[0] == 1:
            return result(0)
        else:
            return IMPOSSIBLE

    while True:
        # If we have double or more of one kind of bomb over the other, that means we are
        # able to take a shortcut. In this case, we'd normally minus small quantity from the larger
        # several times in a row. Instead of doing that iteration one by one, we can divide and jump
        # forward several iterations.
        sm, lg = sorted(bombset)  # find larger and smaller numbers
        divider = (lg - sm) / sm
        # Don't let divider be zero. If it is, we're just going to minus smaller quantity bomb type
        # from larger just once.
        divider = max(divider, 1)
        iteration += divider
        bombset = [sm, lg - (divider * sm)]

        # check if we've hit our starting bomb count of [1,1]. If so, we've found our answer.
        if bombset[0] == bombset[1] == 1:
            return result(iteration)

        # check if any of the bomb types have reached zero or less. If so, we can now conclude that
        # its not possible to find workable solution.
        if any(x < 1 for x in bombset):
            return IMPOSSIBLE


def check(ans, M, F):
    obtained_answer = answer(M,F)
    if ans == obtained_answer:
        print "Correct"
    else:
        print "Expected: %s | Obtained: %s" % (ans, obtained_answer)

check("0", "1", "1")
check("49", "1", "50")
check("1", "2", "1")
check("4", "4", "7")
check("10", "31", "4")
check(IMPOSSIBLE, "32", "4")
check("29", "580", "723")
check("27", "1004", "1087")
