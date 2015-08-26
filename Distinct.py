__author__ = 'jmasramon'

# returns the number of distinct values in array A
#
#         N is an integer within the range [0..100,000];
#         each element of array A is an integer within the range [-1,000,000..1,000,000].

def solution(A):
    n = len(A)
    num = 0
    if n == 0:
        return num
    num = 1
    A.sort()
    for i in xrange(1, n):
        if A[i] != A[i - 1]:
            num += 1
    return num


def seq_all_eq_except_positions(n, exceptions, positions, rest):
    orig_n = n
    while (n > 0):
        for i in xrange(len(exceptions)):
            if n == (orig_n - positions[i]):
                # print 'yielding exception'
                yield exceptions[i]
                del exceptions[i]
                del positions[i]
                break
        yield rest
        n -= 1


assert solution([10, 2, 5, 1, 8, 20]) == 6
assert solution([2, 3, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 4
assert solution([]) == 0
assert solution([1]) == 1
assert solution([1, 2]) == 2
assert solution([-1000000, 1000000]) == 2
assert solution(list(seq_all_eq_except_positions(100000, [], [], 1))) == 1
print solution(list(seq_all_eq_except_positions(100000, [2,3,4], [10,30,40], 1)))
assert solution(list(seq_all_eq_except_positions(100000,[2,3,4], [10,30,40], 1))) == 4
