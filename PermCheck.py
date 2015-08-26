__author__ = 'jmasramon'

def solution(A):
    # print A
    n = len(A)
    found = [0]*n
    num_found = 0
    for i in xrange(n):
        # print i, A[i], found
        if A[i] > n:
            return 0
        if found[A[i]-1] == 0:
            num_found += 1
            if num_found == n:
                return 1
            found[A[i]-1] = 1
    return 0

assert solution([4,1,3,2]) == 1
assert solution([4,1,3]) == 0
assert solution([4,1,3,1000000000]) == 0
assert solution([4,1,3,2,5,6,7,8,9,10,11,12,15,14,13,20,19,18,17,16]) == 1
assert solution([4,2,3,2]) == 0
assert solution([1]) == 1
assert solution([2]) == 0


