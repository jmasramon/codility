__author__ = 'jmasramon'

# todo solve this one
def solution(A):
    A = remove_negatives(A)

    n = len(A)
    existing_minimal = 2147483647
    for i in xrange(n):
        if A[i]>0 and A[i] < existing_minimal:
            existing_minimal = A[i]
    return 5

def remove_negatives(A,n):
    for i in xrange(n):
        print i, A[i]
        if A[i] < 0:
            del A[i]
    return A

# assert (primesSmallerThanN([1,3,6,4,1,2]) == 5)
# assert (primesSmallerThanN([]) == 1)
# assert (primesSmallerThanN([]) == 1)
# assert (primesSmallerThanN([]) == 1)
# assert (primesSmallerThanN([]) == 1)
# assert (primesSmallerThanN([]) == 1)

print remove_negatives([-1,-2,3,-1,34,56,-2],7)
assert (remove_negatives([-1,-2,3,-1,34,56,-2],7) == [3,34,56])