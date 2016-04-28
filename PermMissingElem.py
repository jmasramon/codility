__author__ = 'jmasramon'

# A[N] integers in range [1,(N+1)]
def solution1(A):
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

def solution2(A): # not working for all values due to misunderstanding of requs
    n = len(A)
    if n <= 1: return 1
    sA = sorted(A)
    prev = sA[0]
    if prev != 1: return 1
    for e in sA[1:]:
        if not (e - prev) == 1:
            return prev + 1
        prev = e

def solution(A):
    n = len(A)
    # if n <= 1: return 1
    total = 0
    for elem in xrange(1,n+2):
        total ^= elem
    for elem in A:
        total ^= elem
    return total

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

