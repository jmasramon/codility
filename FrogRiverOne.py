__author__ = 'jmasramon'

# Find the earliest time when a frog can jump to the other side of a river.
# initial pos 0
# final pos x belong to 1..100000
# array[N] N belong to 1..100000
# A[K] position of leave in t=K s belong to 1..X
# earliest time? =
# no soultion -> -1

def solution(X, A):
    n = len(A)
    found = [0]*X
    num_found = 0

    for i in xrange(n):
        if found[A[i]-1] == 0:
            num_found += 1
            found[A[i]-1] = 1
        # print i,A[i],found
        if num_found == X:
            return i
    return -1


# print primesSmallerThanN(5, [1,3,1,4,2,3,5,4])
assert solution(5, [1,3,1,4,2,3,5,4]) == 6
assert solution(5, [1,3,1,4,2,3,5,4,5,3,2,5]) == 6
assert solution(5, [1,3,1,4,2,3,2,4]) == -1
assert solution(5, [2,3,5,4,2,3,5,4]) == -1
assert solution(5, [5,4,3,2,1,3,2,4]) == 4
