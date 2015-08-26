__author__ = 'jmasramon'

def solution(A):
    n = len(A)
    if n < 3:
        return 0
    A.sort()
    for i in xrange(0, n-2):
        if A[i]+A[i+1] > A[i+2] and A[i+1]+A[i+2] > A[i] and A[i]+A[i+2] > A[i+1]:
            return 1
    return 0


def seq_all_eq_except_first(n, first, rest):
    yield first
    n -= 1
    while(n>0):
        yield rest
        n -= 1

def seq_all_eq_except_positions(n, exceptions, positions, rest):
    orig_n = n
    while(n>0):
        for i in xrange(len(exceptions)):
            if n == (orig_n - positions[i]):
                # print 'yielding exception'
                yield exceptions[i]
                del exceptions[i]
                del positions[i]
                break
        yield rest
        n -= 1


assert solution([10,2,5,1,8,20]) == 1
assert solution([10,50,5,1]) == 0
assert solution([]) == 0
assert solution([1]) == 0
assert solution([1,2]) == 0
assert solution([10,5,8]) == 1
assert solution([-10,-5,-8]) == 0
# assert primesSmallerThanN([-10,-10,-10]) == 1
assert solution([-2147483648, 2147483647, -2147483648, 2147483647]) == 0
assert solution(list(seq_all_eq_except_first(100000,0,0))) == 0
assert solution(list(seq_all_eq_except_positions(35,[10,5,8],[10,20,30], 0))) == 1

