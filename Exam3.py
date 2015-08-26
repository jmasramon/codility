__author__ = 'jmasramon'


def solution(A):
    n = len(A)
    min_add = A[0]
    min_s_sum = 10000
    all_positives = False

    if n == 1:
        return A[0]

    if A[0] > 0:
        all_positives = True

    for i in xrange(1,n):
        if A[i]<0 and all_positives:
            all_positives = False
            min_s_sum = abs(A[i-1] + A[i])
            min_add = min_s_sum
        else:
            min_add = min(abs(min_add), abs(min_add + A[i]))
            min_s_sum = min(min_s_sum, min_add)

        print A[i], min_add, min_s_sum
    return min_s_sum





if __name__ == '__main__':
    print 'Start tests..'
    assert solution([2]) == 2
    assert solution([2,-1]) == 1
    assert solution([2,-4,6,-3,9]) == 1
    assert solution([1,2,3,4]) == 1
    assert solution([-1,-2,-3,-4]) == 1
    assert solution([1,2,3,4,-1,-2,-3,-4]) == 1
    assert solution([-1,-2,-3,-4,1,2,3,4]) == 1
    assert solution([-2,-3,-4,1,2,3,4]) == 1

