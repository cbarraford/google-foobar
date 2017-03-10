
def answer(s):
    # default to one (one really large slice)
    ans = 1
    # try different slice sizes
    for x in xrange(2, 200):
        count = splitIt(s, x)
        if count > ans:
            ans = count

        if x >= len(s)/2:
            return ans

    return ans

def splitIt(s,num):
    # we need equals slices, so check modulo
    if len(s) % num != 0:
        return 0

    # break string into equal parts
    mylist = list(map(''.join, zip(*[iter(s)]*num)))

    # force list uniqueness and count number of unique. Looking for 1 here.
    if len(set(mylist)) == 1:
        return len(mylist)

    return 0


print answer("ab" * 5)
print answer("abc" * 5)
print answer("abcd" * 5)
print answer("abcde" * 5)
