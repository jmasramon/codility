# coding=utf-8
__author__ = 'jmasramon'

# product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).
# find the maximal product of any triplet

        # N (len(A)) is an integer within the range [3..100,000];
        # each element of array A is an integer within the range [−1,000..1,000].


def solution(A):
    orig = A
    n = len(A)
    A.sort()
    print orig, '->', A
    res = max(A[n-1]*A[n-2]*A[n-3], A[0]*A[1]*A[n-1])

    return res



# print primesSmallerThanN([-3,1,2,-2,5,6])
assert solution([-3,1,2,-2,5,6]) == 60

print solution([-9,-9,-9,2,5,6])
# assert primesSmallerThanN([-9,-9,-9,2,5,6]) == 486

assert solution([-1000,-1000,-1000]) == -1000000000

assert solution([-1000,1000,-1000]) == 1000000000

print solution([-1000,-1000,1000,1000])
# assert primesSmallerThanN([-1000,-1000,1000,1000]) == 1000000000

print solution([-2000,-1000,-10,-10,10,10,1000])
# assert primesSmallerThanN([-2000,-1000,-10,-10,10,10,1000]) == 100000

# print primesSmallerThanN([-2000,-1000,-10,-10,-10,-10,-10])
assert solution([-2000,-1000,-10,-10,-10,-10,-10]) == -1000

print solution([-1000,1000,0,-1000,1000])
assert solution([-1000,1000,0,-1000,1000]) == 1000000000

assert solution([0,0,0]) == 0

assert solution([0,3,7]) == 0
