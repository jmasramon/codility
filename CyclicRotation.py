__author__ = 'jmasramon'

def solution(A, K):
    n = len(A)
    if n>1:
        while(K):
            last = A[n-1]
            for i in xrange(n-1):
                A[n-1-i] = A[n-1-i-1]
            A[0] = last
            K -= 1
    return A


if __name__ == '__main__':
    print 'Start tests..'
    print solution([1,2,3], 1)
    print solution([1,2,3], 2)
    print solution([1,2,3], 3)
    print solution([1,2,3], 4)
    print solution([1,2,3], 5)

    assert solution( [3, 8, 9, 7, 6],3) ==  [9, 7, 6, 3, 8]
    assert solution( [],3) ==  []
    assert solution( [1,2,4],0) ==  [1,2,4]
    assert solution( [3, -8, 9, -7, 6],3) ==  [9, -7, 6, 3, -8]
