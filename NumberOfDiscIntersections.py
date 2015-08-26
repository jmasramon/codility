# coding=utf-8
__author__ = 'jmasramon'


# We draw N discs on a plane. The discs are numbered from 0 to N − 1. A zero-indexed array A of
# N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn
# with its center at (J, 0) and radius A[J].
#
# We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at
# least one common point (assuming that the discs contain their borders).

        # N is an integer within the range [0..100,000];
        # each element of array A is an integer within the range [0..2,147,483,647].

# returns the number of (unordered) pairs of intersecting discs.
# The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

# todo finish with https://codility.com/demo/results/demo8PBJQN-53G/

def solution(A):
    n = len(A)
    res = 0
    A_bis = [None]*n
    for i in xrange(n):
        A_bis[i] = (A[i],i)
    A_bis.sort(key=lambda tup: -tup[0])
    # print A, '->', A_bis

    while (len(A_bis)>0):
        left = leftLimit(A_bis[0])
        right = rightLimit(A_bis[0])

        for i in xrange (1,len(A_bis)):
            # print 'checking'
            l_to_check = leftLimit(A_bis[i])
            r_to_check = rightLimit(A_bis[i])
            if  r_to_check >= left and r_to_check <= right or l_to_check <= right and l_to_check >= left:
                res += 1
        del A_bis[0]
        # print '->', A_bis
    return res

def leftLimit(t):
    return t[1]-t[0]

def rightLimit(t):
    return t[1]+t[0]

def seq_all_eq_except_positions(n, exceptions, positions, rest):
    orig_n = n
    while (n > 0):
        for i in xrange(len(exceptions)):
            if n == (orig_n - positions[i]):
                yield exceptions[i]
                del exceptions[i]
                del positions[i]
                break
        yield rest
        n -= 1


if __name__ == '__main__':
    print 'Start tests..'
    # print primesSmallerThanN([1,5,2,1,4,0])
    assert solution([1,5,2,1,4,0]) == 11
    assert solution([]) == 0
    assert solution([1]) == 0
    # assert primesSmallerThanN(list(seq_all_eq_except_positions(100000,[],[],1))) == 100000


# l = [(1,0),(5,1),(2,2),(1,3),(4,4),(0,5)]
# print l
# l.sort()
# print l
# l.sort(key=lambda tup: -tup[0])
# print l
