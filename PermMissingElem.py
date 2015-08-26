__author__ = 'jmasramon'

# A[N] integers in range [1,(N+1)]
def solution(A):
    A.sort()
    n = len(A)
    print 'sorted A:', A, 'len:', n
    if n == 0 or A[0] != 1:
        return 1
    if n == 1:
        return 2
    if A[n-1] != n+1:
        return n+1
    for i in xrange(n-1):
        print A[i], A[i+1]
        if (A[i+1]-A[i])>1:
            return A[i]+1


# print primesSmallerThanN([2,3,1,5])
# print primesSmallerThanN([])
# print primesSmallerThanN([1])
assert solution([1]) == 2
assert solution([2]) == 1
assert solution([1,2]) == 3
assert solution([2,3]) == 1
# print primesSmallerThanN([2,3,4,5])
assert solution([2,3,4,5]) == 1
# print primesSmallerThanN([2,3,4,1])
assert solution([2,3,4,1]) == 5

