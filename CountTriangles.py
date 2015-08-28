__author__ = 'jmasramon'


def solution(A): # naive solution
    count = 0
    n = len(A)

    def test_a():
        return A[p] + A[q] > A[r]

    def test_b():
        return A[q] + A[r] > A[p]

    def test_c():
        return A[r] + A[p] > A[q]

    for p in xrange(n-2):
        for q in xrange(p+1,n-1):
            for r in xrange(q+1, n):
                if test_a() and test_b() and test_c():
                    count += 1
    return count

def fast_solution(A):
    count = 0
    n = len(A)

    A.sort()
    # print A

    for p in xrange(n-2):
        for q in xrange(p+1, n-1):
            r = q + 1
            # print p,q,r,'->',A[p],A[q],A[r]
            while r < n and A[r] < A[p] + A[q]:
                # print 'good one'
                r += 1
            # print '  ->', q,r
            count += r - q - 1
    return count


if __name__ == '__main__':
    print 'Start tests..'
    assert solution([10, 2, 5, 1, 8, 12]) == 4

    assert fast_solution([10, 2, 5, 1, 8, 12]) == 4
