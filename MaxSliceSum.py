__author__ = 'jmasramon'

def solution(A):
    n = len(A)
    max_add = 0
    max_s_sum = 0
    all_neg = False
    if n == 1:
        return A[0]
    if A[0] < 0:
        all_neg = True
        max_s_sum = A[0]
    for a in A:
        if all_neg and a > 0:
            all_neg = False
        if all_neg:
            max_s_sum = max(max_s_sum, a)
        else:
            max_add = max(0, max_add + a)
            max_s_sum = max(max_s_sum, max_add)
    return max_s_sum

def alternateSolution(A):
    max_slice_ending_here = A[0]
    max_slice = A[0]

    for element in A[1:]:
        max_slice_ending_here = max(element, max_slice_ending_here+element)
        max_slice = max(max_slice, max_slice_ending_here)

    return max_slice

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
    assert solution([3, 2, -6, 4, 0]) == 5
    assert solution([3]) == 3
    assert solution([3,-3]) == 3
    assert solution([-3,3]) == 3
    assert solution([-3,-2]) == -2
    assert solution([-3,-2,-4]) == -2
    assert solution([-3,-3,-3]) == -3
    assert solution([-3,-3,0,-3]) == 0
    assert solution([0,3]) == 3
    assert solution([0,-3]) == 0
    assert solution([-3]) == -3
    assert solution([1000000, 1000000]) == 2000000
    assert solution(list(seq_all_eq_except_positions(2148,[483647],[0],1000000))) == 2147483647

    # assert AlternateSolution([3, 2, -6, 4, 0]) == 5
    assert alternateSolution([3]) == 3
    assert alternateSolution([3,-3]) == 3
    assert alternateSolution([-3,3]) == 3
    assert alternateSolution([-3,-2]) == -2
    assert alternateSolution([-3,-2,-4]) == -2
    assert alternateSolution([-3,-3,-3]) == -3
    assert alternateSolution([-3,-3,0,-3]) == 0
    assert alternateSolution([0,3]) == 3
    assert alternateSolution([0,-3]) == 0
    assert alternateSolution([-3]) == -3
    assert alternateSolution([1000000, 1000000]) == 2000000
    assert alternateSolution(list(seq_all_eq_except_positions(2148,[483647],[0],1000000))) == 2147483647
