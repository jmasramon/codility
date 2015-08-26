__author__ = 'jmasramon'


def solution(A):
    n = len(A)

    if n< 4:
        return -1

    cur_dpt = -1
    p = 0
    r = -1
    q = -1

    for i in xrange(n):
        if q < 0 and A[i] >= A[i - 1]:
            q = i - 1
        if (0 <= q > r) and (A[i] <= A[i - 1] or i + 1 == n):
            r = i - 1
            cur_dpt = max(cur_dpt, min(A[p] - A[q], A[r] - A[q]))
            p = i - 1
            q = -1
            r = -1
    if cur_dpt > 0:
        return cur_dpt
    return -1


def seq_all_eq_except_positions(n, exceptions, positions, rest):
    orig_n = n
    orig_exceps = len(exceptions)
    exception_found = False
    processed_exceptions = 0
    while (n > 0):
        exception_found = False
        for i in xrange(len(exceptions)):
            processed_exceptions += 1
            if n == (orig_n - positions[i]):
                yield exceptions[i]
                del exceptions[i]
                del positions[i]
                exception_found = True
                break
        if not exception_found and processed_exceptions == orig_exceps:
            yield rest
        n -= 1


if __name__ == '__main__':
    print 'Start tests..'
    assert solution([0, 1, 3, -2, 0, 1, 0, -3, 2, 3]) == 4
    assert solution([0, 1, 3, -2, -3, -4, 0, 1, 2, 3]) == 6
    assert solution([0, 1, 3, -2, -3, -4, 0, 1, 2, 3, 4]) == 7
    assert solution([0]) == -1
    assert solution([0, 1]) == -1
    assert solution([1, 0, 1]) == -1
    assert solution([1, 0, 1, 2]) == 1
    assert solution([4, 0, 1, 2]) == 1
    assert solution([1000000, 0, 1000000, 2]) == 1000000
    assert solution([1000000000, 0, 1000000000, 2]) == 1000000000
    assert solution(list(seq_all_eq_except_positions(1000000, [], [], 1))) == -1
