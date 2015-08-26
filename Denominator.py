# coding=utf-8
__author__ = 'jmasramon'

        # N is an integer within the range [0..100,000];
        # each element of array A is an integer within the range [−2147483648..2,147,483,647].



def solution(A):
    n = len(A)
    if n == 0:
        return -1
    if n == 1:
        return 0
    candidate = A[0]
    candidate_count = 1
    candidate_index = 0
    for i in xrange(1,n):
        if A[i] == candidate:
            candidate_count += 1
            if candidate_count > n // 2:
                return candidate_index
        else:
            if candidate_count > 0:
                candidate_count -= 1
            else:
                candidate = A[i]
                candidate_index = i
                candidate_count = 1
            if candidate_count == 0:
                candidate = -1
    if candidate_count > 1 or candidate == -1:
        return candidate_index
    else:
        candidate_count = 0
        for i in xrange(n):
            if A[i] == candidate:
                candidate_count += 1
        if candidate_count > n // 2:
            return candidate_index
        return -1


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
    assert solution([]) == -1
    sol1 = solution([3,4,3,2,3,-1,3,3])
    assert (sol1 == 0 or sol1 == 2 or sol1 == 4 or sol1 == 6 or sol1 == 7)
    sol2 =  solution([4,3,3,2,3,-1,3,3])
    assert (sol2 == 1 or sol1 == 2 or sol1 == 4 or sol1 == 6 or sol1 == 7)
    assert solution([2147483648,2147483648,-2147483648]) == 0

